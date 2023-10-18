
import requests

# mini Challenge    
# create a script that allows you to interactively
# update a task via its ID>

# Acceptance criteria
# 1. Prompt the user for an ID
# 2. Issue a get request for the specific task
# 3. Display the task in question
# 4. Allow the user to update all of the fields (Via prompts)

# Bonus:
# 1. If there is no task received (404) display an error message.

# Note: the methods in requests for PUT and GET are "requests.put(URL, json=something)"
# and requestsget(URL)

BACKEND_URL = "http://127.0.0.1:5000/tasks"

def get_task_by_id(task_id):
    response = requests.get(f"{BACKEND_URL}/{task_id}")
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Task with ID {task_id} not found.")
        return None

def update_task(task_id, updated_task):
    response = requests.put(f"{BACKEND_URL}/{task_id}", json=updated_task)
    if response.status_code == 204:
        print("Update succeeded.")
    else:
        print("Update failed.")

if __name__ == "__main__":
    task_id = input("Enter the ID of the task you want to update: ")
    task = get_task_by_id(task_id)
    task = task.get("task")
    if task:
        print("Current task details:")
        print(task)
        updated_task = {}
        for key in task:
            updated_task[key] = input(f"Enter the new {key} (current: {task[key]}): ")
        update_task(task_id, updated_task)