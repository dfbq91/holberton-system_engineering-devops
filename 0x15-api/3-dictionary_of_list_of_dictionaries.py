#!/usr/bin/python3
'''Given an api, returns information about a
TODO list progress'''


import json
import requests
from sys import argv


if __name__ == "__main__":

    jsoned_users = requests.get('https://jsonplaceholder.typicode.com/users/')\
        .json()
    jsoned_todos = requests.get('https://jsonplaceholder.typicode.com/todos')\
        .json()
    file_name = "todo_all_employees.json"

    user_id_dict = {}
    user_id_name_dict = {}
    for user in jsoned_users:
        id = user.get('id')
        user_id_dict[id] = []
        user_id_name_dict[id] = user.get('username')

    for task in jsoned_todos:
        task_by_id = {}
        id = task.get("userId")
        task_by_id = {"username": user_id_name_dict.get(id),
                      "task": task.get('title'),
                      "completed": task.get('completed')}
        user_id_dict.get(id).append(task_by_id)

    # Write in json file
    with open(file_name, 'w') as f:
        json.dump(user_id_dict, f)
