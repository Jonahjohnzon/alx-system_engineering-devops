#!/usr/bin/python3
"""Function print hot posts on given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of 10 hottest posts on subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    resp = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if resp.status_code == 404:
        print("None")
        return
    res = resp.json().get("data")
    [print(c.get("data").get("title")) for c in res.get("children")]
