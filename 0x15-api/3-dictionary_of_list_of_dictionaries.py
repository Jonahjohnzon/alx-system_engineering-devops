#!/usr/bin/python3
"""Export to-do list"""
import json
import requests

if __name__ == "__main__":
    ul = "https://jsonplaceholder.typicode.com/"
    user = requests.get(ul + "users").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(ul + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in user}, jsonfile)
