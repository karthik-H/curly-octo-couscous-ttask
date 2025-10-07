# task_manager.py

_tasks = []
_next_id = 1


def create_task(title):
    global _next_id
    if not isinstance(title, str):
        raise TypeError("Title must be a string.")
    if title == "":
        raise ValueError("Title cannot be empty.")
    task = {"id": _next_id, "title": title}
    _tasks.append(task)
    _next_id += 1
    return task


def get_all_tasks():
    return list(_tasks)


def get_task(task_id):
    for task in _tasks:
        if task["id"] == task_id:
            return task
    return None


def update_task(task_id, new_title):
    task = get_task(task_id)
    if task:
        task["title"] = new_title
        return True
    return False


def delete_task(task_id):
    global _tasks
    task = get_task(task_id)
    if task:
        _tasks = [t for t in _tasks if t["id"] != task_id]
        return True
    return False