#!/usr/bin/python3
"""Module that recursively queries the Reddit API and counts
occurrences of given keywords in hot article titles.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count keyword occurrences in hot article titles.

    Args:
        subreddit (str): The subreddit name.
        word_list (list): List of keywords to count.
        after (str): Pagination token.
        counts (dict): Dictionary storing keyword counts.

    Returns:
        None
    """
    if counts is None:
        counts = {}
        for word in word_list:
            word = word.lower()
            counts[word] = counts.get(word, 0)

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
            return

        data = response.json().get("data", {})

        for post in data.get("children", []):
            words = post.get("data", {}).get("title", "").lower().split()
            for word in words:
                if word in counts:
                    counts[word] += 1

        after = data.get("after")

        if after is not None:
            return count_words(subreddit, word_list, after, counts)

        sorted_counts = sorted(
            counts.items(),
            key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))

    except (requests.RequestException, ValueError):
        return
