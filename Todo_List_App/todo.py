def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


tasks = load_tasks()

while True:

    print("\n===== TO DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        if not tasks:
            print("No tasks available")

        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":

        task = input("Enter task: ")
        tasks.append(task)

        save_tasks(tasks)

        print("Task added")

    elif choice == "3":

        if not tasks:
            print("No tasks to remove")

        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            index = int(input("Enter task number: ")) - 1

            if 0 <= index < len(tasks):
                removed = tasks.pop(index)

                save_tasks(tasks)

                print(f"{removed} removed")

            else:
                print("Invalid number")

    elif choice == "4":

        print("Exiting...")

        break

    else:
        print("Invalid choice")
        