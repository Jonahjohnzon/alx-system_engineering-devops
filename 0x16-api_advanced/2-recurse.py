#!/usr/bin/python3
"""Function query a list of all hot posts on subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns list of titles of all hot posts on subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    param = {
        "after": after,
        "count": count,
        "limit": 100
    }
    resp = requests.get(url, headers=headers, params=param,
                            allow_redirects=False)
    if resp.status_code == 404:
        return None

    res = resp.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
