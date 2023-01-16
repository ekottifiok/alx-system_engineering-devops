#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
gathers data from API and exports it to JSON file
Implemented using recursion
"""
import json
import requests


REST_API = "https://jsonplaceholder.typicode.com"


def main():
    users_res = requests.get('{}/users'.format(REST_API)).json()
    todos_res = requests.get('{}/todos'.format(REST_API)).json()
    users_data = dict()
    for user in users_res:
        id = user.get('id')
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))
        users_data[id] = list(map(
            lambda x: {
                'username': user.get('username'),
                'task': x.get('title'),
                'completed': x.get('completed')
            }, todos
        ))
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)


if __name__ == '__main__':
    main()
