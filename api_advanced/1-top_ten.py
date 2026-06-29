#!/usr/bin/python3
"""Module that queries the Reddit API and prints the titles of the
first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.
    If the subreddit is invalid, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (custom-reddit-script/1.0)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        results = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not results:
        print(None)
        return

    for post in results:
        print(post.get("data", {}).get("title"))
