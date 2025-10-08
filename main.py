# main.py

import task_manager


def create(title):
    if not title or not title.strip():
        return {"error": "Title cannot be empty."}
    task = task_manager.create_task(title.strip())
    return {"success": True, "task": task}


def list_tasks():
    return {"tasks": task_manager.get_all_tasks()}


def update(task_id, new_title):
    if not isinstance(task_id, int):
        return {"error": "Task ID must be an integer."}
    if not new_title or not new_title.strip():
        return {"error": "New title cannot be empty."}
    if task_manager.update_task(task_id, new_title.strip()):
        return {"success": True}
    return {"error": f"Task with ID {task_id} not found."}


def delete(task_id):
    if not isinstance(task_id, int):
        return {"error": "Task ID must be an integer."}
    if task_manager.delete_task(task_id):
        return {"success": True}
    return {"error": f"Task with ID {task_id} not found."}