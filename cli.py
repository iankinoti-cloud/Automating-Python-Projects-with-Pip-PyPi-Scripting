import argparse

from lib.generate_log import generate_log
from lib.task_manager import TaskManager


def build_parser():
    parser = argparse.ArgumentParser(description="Task management CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")

    complete_parser = subparsers.add_parser("complete-task", help="Mark a task as complete")
    complete_parser.add_argument("task_id", type=int, help="ID of the task to complete")

    subparsers.add_parser("list-tasks", help="List all tasks")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add-task":
        task = manager.add_task(args.description)
        print(f"Added task {task.task_id}: {task.description}")
        generate_log([f"Added task {task.task_id}: {task.description}"])

    elif args.command == "complete-task":
        task = manager.complete_task(args.task_id)
        print(f"Completed task {task.task_id}: {task.description}")
        generate_log([f"Completed task {task.task_id}: {task.description}"])

    elif args.command == "list-tasks":
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        for task in tasks:
            print(task)


if __name__ == "__main__":
    main()
