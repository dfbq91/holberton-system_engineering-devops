#!/usr/bin/python3
'''Tasks with subreddit api'''
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''Queries the Reddit API and returns all
    hot posts listed for a given subreddit'''

    # Set url with query string, do request and covert it to json
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.\
        format(subreddit, after)
    headers = {'User-Agent': 'Python3'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    r_jsoned = r.json()

    # if the subreddit exists... otherwise return None
    if r.status_code != 200:
        return None

    # check if the subreddit has posts
    if r_jsoned.get('data').get('children') is None:
        return None

    # Set after to get next page with 25 posts and validate it exists
    after = r_jsoned.get('data').get('after')

    # Get titles of posts in a hot_list iterating in the page and
    # with recursion traverse all pages in group of the length of each page
    for post_number in range(0, len(r_jsoned.get('data').get('children'))):
        hot_list.append(r_jsoned.get('data').get('children')[post_number].
                        get('data').get('title'))

    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
