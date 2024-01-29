#!/usr/bin/python3
"""Return to-do list"""
import requests
import sys

if __name__ == "__main__":
    ur = "https://jsonplaceholder.typicode.com/"
    user = requests.get(ur + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(ur + "todos", params={"userId": sys.argv[1]}).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
