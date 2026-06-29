#!/usr/bin/python3
"""Module that queries the Reddit API and prints the titles of the
first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    If the subreddit is invalid, print None.
    """
    if subreddit is None or not isinstance(subreddit, str) or subreddit == "":
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0.0.0 Safari/537.36"
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

    # Invalid subreddits return a redirect (302) to a search page,
    # or sometimes a 404 directly.
    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
    except ValueError:
        print(None)
        return

    results = data.get("data", {}).get("children", [])

    if not results:
        print(None)
        return

    for post in results:
        print(post.get("data", {}).get("title"))


if __name__ == "__main__":
    top_ten("programming")
