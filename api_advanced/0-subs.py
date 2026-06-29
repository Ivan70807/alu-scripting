#!/usr/bin/python3
"""Module for querying the Reddit API."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:reddit-api:v1.0 (by /u/example)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            return 0

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
