

import json
import os


TASKS_FILE = "todo_tasks.json"    


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)


def show_tasks(tasks):
    if not tasks:
        print("your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            status = "✔" if task["done"] else "✘"
            print(f"{i+1}. {task['title']} [{status}]")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task description: ")
            tasks.append({"title": title, "done": False})
            print("Task added.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                tasks[index]["done"] = True
                print("Task marked as done.")
            except:
                print("Invalid task number.")
        elif choice == "4":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                removed = tasks.pop(index)
                print(f"Deleted task: {removed['title']}")
            except:
                print("Invalid task number.")
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Please enter a valid option.")
 
if __name__== "__main__":
       main()
