"""
this is a todo list application
users can add or remove tasks and see their list of tasks
"""

task_name_list = []
task_description_list = []


def add_task(name, description):
    task_name_list.append(name)
    task_description_list.append(description)


def remove_task(task, task_id):
    if task is None:
        return None
    for i in range(len(task)):
        if i == task_id:
            del task[i]
            return task
    return task


def task_creator(name_list, description_list):
    task = {}
    for i in range(len(name_list)):
        task[i] = {"name": name_list[i], "description": description_list[i]}
    return task


def todo_list():
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            task_description = input("Enter the task description: ")
            add_task(task_name, task_description)
            print("Task added successfully!")

        elif choice == "2":
            try:
                task_id = int(input("Enter the task ID to remove: "))
                remove_task(
                    task_creator(task_name_list, task_description_list), task_id
                )
                print("Task removed successfully!")
            except IndexError:
                print("Task not found.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "3":
            tasks = task_creator(task_name_list, task_description_list)
            for i, task in tasks.items():
                print(f"Task ID: {i}")
                print(f"Name: {task['name']}")
                print(f"Description: {task['description']}")
            print("-------------------------")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


todo_list()
