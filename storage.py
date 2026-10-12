import json


def storage_save(tasks_list):
    with open("tasks.json", "w") as task_data:
        json.dump(tasks_list, task_data, indent=4)
