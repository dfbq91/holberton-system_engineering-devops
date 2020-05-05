#!/usr/bin/python3
'''Given an api, returns information about a
TODO list progress'''


import json
import requests
from sys import argv


if __name__ == "__main__":

    jsoned_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                               format(argv[1])).json()
    jsoned_todos = requests.get('https://jsonplaceholder.typicode.com/todos').\
        json()

    # Get name of the employee and set filename
    username = jsoned_user.get('username')
    id = jsoned_user.get('id')
    file_name = "{}.json".format(id)

    # Prepare json with all tasks and list with all tasks
    tasks_by_id = {}
    json_tasks_list = []

    for tasks in jsoned_todos:
        json_task = {}
        if id == tasks.get('userId'):
            json_task["task"] = tasks.get('title')
            json_task["completed"] = tasks.get('completed')
            json_task["username"] = username
            json_tasks_list.append(json_task)

    tasks_by_id[id] = json_tasks_list

    with open(file_name, 'w') as f:
        json.dump(tasks_by_id, f)
