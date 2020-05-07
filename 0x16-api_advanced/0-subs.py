#!/usr/bin/python3
'''Tasks with subreddit api'''
import requests


def number_of_subscribers(subreddit):
    '''queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My name is Diego'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        jsoned_r = r.json()
        return jsoned_r.get('data').get('subscribers')
    else:
        return 0
