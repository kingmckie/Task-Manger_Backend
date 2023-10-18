import requests

BACKEND_URL = "http://127.0.0.1:5000/tasks"

def create_task(summary, descripion):
    task = {
        "summary": summary,
        "description": descripion
    }

    response = requests.post(BACKEND_URL, json=task)
    if response.status_code == 201:
        print("Creation succeeded.")
    else:
        print("Creation failed.")

if __name__=="__main__":
    print("Fill out the promts below to create a new task:")
    summary = input("New task summary:")
    description = input("New ")
    create_task(summary, description)