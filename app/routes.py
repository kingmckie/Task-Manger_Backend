from flask import Flask, request
from app.database import task
from datetime import datetime

app = Flask(__name__)
@app.get("/")
def index():
    return {
        "ok": True,
        "timestamp": datetime.now().strftime("%F %H:%M:%S")
    }

@app.get("/tasks")
def get_all_task():
    tasks = task. scan()
    out = {
        "ok": True,
        "tasks": tasks
    }

    return out

@app.get("/tasks/<int:pk>")
def get_task_by_id(pk):
    single_task = task.select_by_id(pk)
    if not single_task:
        return{"ok": False, "message": "Not found"}, 404
    out = {
        "task": single_task,
        "ok": True
    }
    return out

@app.post("/tasks")
def creat_task():
    task_data = request.json
    task.insert(task_data)
    out = {
        "ok": True,
        "message": "Success"
    }

    return out, 201

@app.put("/tasks/<int:pk>")
def update_task(pk):
    task_data = request.json
    task.update (task_data, pk)
    return "", 204

@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete(pk)
    return "", 204