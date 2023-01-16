#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
gathers data from API and exports it to CSV file
Implemented using recursion
"""
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
    with open('{}.csv'.format(id), 'w') as file:
        for todo in todos:
            file.write(
                '"{}","{}","{}","{}"\n'.format(
                    id,
                    user_name,
                    todo.get('completed'),
                    todo.get('title')
                ))


if __name__ == '__main__':
    main()
