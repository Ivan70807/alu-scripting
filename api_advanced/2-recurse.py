#!/usr/bin/python3
"""Module that recursively queries the Reddit API to retrieve
the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a subreddit.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): Accumulates the titles of hot posts.
        after (str): Token used for Reddit API pagination.

    Returns:
        list: A list of hot article titles.
        None: If the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:api-advanced:v1.0 (by /u/reddit_api_project)"
    }
    params = {
        "limit": 100,
        "after": after
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})

        for post in data.get("children", []):
            hot_list.append(post.get("data", {}).get("title"))

        after = data.get("after")

        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except (requests.RequestException, ValueError):
        return None
