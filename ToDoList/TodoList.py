import json

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print(" No tasks available.")
    else:
        print("\n To-Do List:")
        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"[{task['id']}] {task['description']} - {status}")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks(tasks)
            print(f" Task {task_id} updated.")
            return
    print("Task not found.")

def mark_completed(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as completed.")
            return
    print("Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f" Task {task_id} deleted.")

def main():
    while True:
        print("\n To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_id = int(input("Enter task ID to update: "))
            new_desc = input("Enter new description: ")
            update_task(task_id, new_desc)
        elif choice == "4":
            view_tasks()
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_completed(task_id)
        elif choice == "5":
            view_tasks()
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "6":
            print(" Exiting To-Do List. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
