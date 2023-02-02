#!/usr/bin/python3
"""Module for task 3"""
import http.client
from json import loads

def count_words(subreddit, word_list: list, word_count={}, after=None):
    """Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts
    of the subreddit"""

    conn = http.client.HTTPSConnection("www.reddit.com")

    headersList = {
        "Accept": "*/*",
        "User-Agent": "My-User-Agent"
    }
    payload = ""
    conn.request("GET", "/r/{}/hot.json?after={}".
                 format(subreddit, after), payload, headersList)
    
    data = conn.getresponse()
    if data.status != 200:
        return None

    data = loads(data.read()).get('data')
    child = data.get('children')
    hot_l = [items.get("data").get("title") for items in child]
    if not hot_l:
        return None

    if word_count == {}:
        word_count = dict.fromkeys(word_list, 0)

    for title in hot_l:
        for word in word_list:
            if word.lower() in title.lower():
                word_count[word] += 1
    if data.get('after'):
        return count_words(subreddit, word_list, word_count, data.get('after'))
    
    word_count = sorted(word_count.items(), key=lambda kv:kv[1], reverse=True)
    [print('{}: {}'.format(k, v)) for k, v in word_count if v != 0]

