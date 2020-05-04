#!/usr/bin/python3
'''Given an api, returns information about a
TODO list progress'''


import requests
from sys import argv


if __name__ == "__main__":

    done_tasks = 0
    total_tasks = 0
    jsoned_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                               format(argv[1])).json()
    jsoned_todos = requests.get('https://jsonplaceholder.typicode.com/todos').\
        json()

    # Get name of the employee
    name = jsoned_user.get('name')
    id = jsoned_user.get('id')

    # Get total and done tasks number
    for tasks in jsoned_todos:
        if id == tasks.get.get('userId'):
            total_tasks += 1
            if tasks.get('completed') is True:
                done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, done_tasks, total_tasks))

    # Completed tasks
    for tasks in jsoned_todos:
        if id == tasks.get('userId') and tasks.get('completed') is True:
            print("\t{}".format(tasks.get('title')))
