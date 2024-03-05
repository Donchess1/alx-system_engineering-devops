#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    with requests.session() as client:
        info = client.get(url, headers=headers, allow_redirects=False).json()
        try:
            return info.get('data', {}).get('subscribers', 0)
        except Exception:
            return 0
