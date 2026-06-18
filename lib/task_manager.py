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
