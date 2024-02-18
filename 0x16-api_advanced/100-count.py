#!/usr/bin/python3
"""Function counts words in all hot posts of subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Print counts of given words found in hot posts of subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/jonah)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        tit = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in tit:
                tim = len([t for t in tit if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = tim
                else:
                    instances[word] += tim

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
