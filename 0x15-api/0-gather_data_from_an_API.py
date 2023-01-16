#!/usr/bin/python3
"""A script that gathers employee name completed
tasks and total number of tasks from an API
"""

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def main():
    if len(sys.argv) < 2 and not str.isdigit(sys.argv[1]):
        return
    id = int(sys.argv[1])
    emp_req = requests.get('{}/users/{}'.format(REST_API, id)).json()
    task_req = requests.get('{}/todos'.format(REST_API)).json()
    tasks = list(filter(lambda x: x.get('userId') == id, task_req))
    completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
    print('Employee {} is done with tasks({}/{}):'.format(
        emp_req.get('name'),
        len(completed_tasks),
        len(tasks)
    ))
    if len(completed_tasks) > 0:
        for task in completed_tasks:
            print('\t {}'.format(task.get('title')))


if __name__ == "__main__":
    main()
