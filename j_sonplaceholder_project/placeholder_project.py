import requests
from requests import get
from pprint import PrettyPrinter

printer = PrettyPrinter

URL = "https://jsonplaceholder.typicode.com/users/1/todos"

def get_title():
    response = requests.get(URL)
    if response.status_code == 200:
        todo_list = response.json()
        titles = []
        for todo in todo_list:
            titles.append(todo["title"])
        return titles
    else:
        raise Exception("Failed to fetch data from the server")
    
titles = get_title()
for title in titles:
    print(title)

def get_completed_status():
    response = requests.get(URL)
    if response.status_code == 200:
        completed_list = response.json()
        completed = []
        for complete in completed_list:
            completed.append(complete["completed"])
        return completed
    else:
        raise Exception("Failed to fetch data from the server")
    
completed = get_completed_status()
for complete in completed:
    print(complete)
    
def get_true():
    response = requests.get(URL)
    if response.status_code == 200:
        completed_true_list = response.json()
        new_true_list = []
        for true_tasks in completed_true_list:
            if true_tasks["completed"] is True:
                new_true_list.append(true_tasks["title"])
        return new_true_list
    else:
        raise Exception("Failed to fetch data from the server")
    
true_list = get_true()
for i, trues in enumerate(true_list):
    print(i + 1, trues)
