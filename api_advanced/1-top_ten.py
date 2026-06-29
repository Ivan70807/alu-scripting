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
        "User-Agent": "python:api-advanced:v1.0 (by /u/reddit_api_project)"
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

        if response.status_code != 200:
            print(None)
            return

        results = response.json().get("data", {}).get("children", [])

        for post in results:
            print(post.get("data", {}).get("title"))

    except (requests.RequestException, ValueError):
        print(None)
