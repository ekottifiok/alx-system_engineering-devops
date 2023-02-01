#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit"""
import http.client
from json import loads


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    conn = http.client.HTTPSConnection("www.reddit.com")

    headersList = {
        "Accept": "*/*",
        "User-Agent": "My-User-Agent"
    }

    payload = ""
    conn.request("GET", "/r/{}/about.json".format(subreddit),
                 payload, headersList)
    data = conn.getresponse()
    if data.status >= 300:
        return 0
    return loads(data.read()).get("data").get("subscribers")
