#!/usr/bin/python3
"""Returns the number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:subreddit.subscribers:v1.0 (by /u/yourusername)"
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
