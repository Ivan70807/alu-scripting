#!/usr/bin/python3
"""Module that queries the Reddit API and returns the number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The total number of subscribers, or 0 if the subreddit
        is invalid or the request fails.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:api-advanced:v1.0 (by /u/reddit_api_project)"
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

    except (requests.RequestException, ValueError):
        return 0
