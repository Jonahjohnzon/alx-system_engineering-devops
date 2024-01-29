#!/usr/bin/python3
"""Export to-do list information"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    u = "https://jsonplaceholder.typicode.com/"
    user = requests.get(u + "users/{}".format(user_id)).json()
    username = user.get("username")
    todo = requests.get(u + "todos", params={"userId": user_id}).json()
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todo]
