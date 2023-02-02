#!/usr/bin/python3
"""Write a function that queries the Reddit API
and prints the titles of the first
10 hot posts listed for a given subreddit."""
import http.client
from json import loads


def top_ten(subreddit):
    """Queries the Reddit API and returns """
    conn = http.client.HTTPSConnection("www.reddit.com")

    headersList = {
        "Accept": "*/*",
        "User-Agent": "My-User-Agent"
    }
    payload = ""
    conn.request("GET", "/r/{}/hot.json?limit=10".format(subreddit),
                 payload, headersList)
    result = loads(conn.getresponse().read()).get('data')
    if (result):
        for title in result.get("children"):
            print((title.get('data').get('title')))
    else:
        print(None)
