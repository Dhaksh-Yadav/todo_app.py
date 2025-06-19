tasks = []


def show_menu():
    print("\n📋 To-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks():
    if not tasks:
        print("⚠️ No tasks yet!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{idx}. {task['task']} - {status}")


def add_task():
    task_name = input("Enter task name: ").strip()
    if task_name:
        tasks.append({"task": task_name, "done": False})
        print("✅ Task added!")
    else:
        print("⚠️ Task name cannot be empty.")


def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("✅ Task marked as done!")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Deleted: {removed['task']}")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


# 🏁 Main Loop
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting app. See you!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()