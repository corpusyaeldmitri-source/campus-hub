import json


def storage_save(tasks_list):
    with open("tasks.json", "w") as task_data:
        json.dump(tasks_list, task_data, indent=4)


def storage_load():
    try:
        with open("tasks.json", "r") as saved_tasks:
            tasks_list = json.load(saved_tasks)
            return tasks_list
    except FileNotFoundError:
        return []
