#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
gathers data from API and exports it to JSON file
Implemented using recursion
"""
import json
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def main():
    if len(sys.argv) < 2 and not str.isdigit(sys.argv[1]):
        return
    id = int(sys.argv[1])
    user_res = requests.get('{}/users/{}'.format(REST_API, id)).json()
    todos_res = requests.get('{}/todos'.format(REST_API)).json()
    user_name = user_res.get('username')
    todos = list(filter(lambda x: x.get('userId') == id, todos_res))
    with open("{}.json".format(id), 'w') as json_file:
        user_data = list(map(
            lambda x: {
                "task": x.get("title"),
                "completed": x.get("completed"),
                "username": user_name
            },
            todos
        ))
        user_data = {"{}".format(id): user_data}
        json.dump(user_data, json_file)


if __name__ == '__main__':
    main()
