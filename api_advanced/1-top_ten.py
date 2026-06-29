#!/usr/bin/python3
"""Module for printing the titles of the first 10 hot Reddit posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit.

    If the subreddit is invalid, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "python:reddit.api:v1.0 (by /u/example)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
