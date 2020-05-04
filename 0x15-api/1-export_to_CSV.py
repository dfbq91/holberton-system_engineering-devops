#!/usr/bin/python3
'''Given an api, returns information about a
TODO list progress'''


import csv
import requests
from sys import argv


if __name__ == "__main__":

    jsoned_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                               format(argv[1])).json()
    jsoned_todos = requests.get('https://jsonplaceholder.typicode.com/todos').\
        json()

    # Get name of the employee
    name = jsoned_user.get('name')
    id = jsoned_user.get('id')
    filename = "{}.csv".format(id)

    # Open and write into .csv file
    with open(filename, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for tasks in jsoned_todos:
            if id == tasks.get('userId'):
                writer.writerow([id, name, tasks.get('completed'),
                                 tasks.get('title')])
