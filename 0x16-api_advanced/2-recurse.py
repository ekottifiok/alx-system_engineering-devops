#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit"""
import http.client
from json import loads


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""

    conn = http.client.HTTPSConnection("www.reddit.com")

    headersList = {
        "Accept": "*/*",
        "User-Agent": "My-User-Agent"
    }
    payload = ""
    conn.request("GET", "/r/{}/hot.json?count={}&after={}".
                 format(subreddit, count, after), payload, headersList)

    data = conn.getresponse()
    if data.status >= 400:
        return None
    data = loads(data.read()).get('data')
    child = data.get('children')
    hot_l = hot_list + [item.get("data").get("title")
                        for item in child]

    if not data.get("after"):
        return hot_l

    return recurse(subreddit, hot_l, data.get("dist"),
                   data.get("after"))
