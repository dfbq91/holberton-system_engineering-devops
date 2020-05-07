#!/usr/bin/python3
'''Tasks with subreddit api'''
import requests


def top_ten(subreddit):
    '''Queries the Reddit API and returns the top 10
    hot posts listed for a given subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My name is Diego'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        jsoned_r = r.json()
        for post_number in range(1, 11):
            print(jsoned_r.get('data').get('children')[post_number].get('data').get('title'))
    else:
        print(None)
