import json
import os

from lib.task import Task

DEFAULT_STORE_PATH = "tasks.json"


class TaskManager:
    def __init__(self, store_path=DEFAULT_STORE_PATH):
        self.store_path = store_path
        self.tasks = self._load()

    def _load(self):
        if not os.path.exists(self.store_path):
            return []
        with open(self.store_path, "r") as file:
            raw_tasks = json.load(file)
        return [Task.from_dict(item) for item in raw_tasks]

    def _save(self):
        with open(self.store_path, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=2)

    def add_task(self, description):
        next_id = max((task.task_id for task in self.tasks), default=0) + 1
        task = Task(next_id, description)
        self.tasks.append(task)
        self._save()
        return task

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_complete()
                self._save()
                return task
        raise ValueError(f"No task found with id {task_id}")

    def list_tasks(self):
        return list(self.tasks)