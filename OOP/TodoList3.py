
class Task:
    # tasks = {0:['task_name','task_desciption']}
    tasks = {}

    def __init__(self, task_id, task_name, task_description):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description

    def add_task(self):
        self.tasks[self.task_id] = [self.task_name, self.task_description]
        return self.tasks

    def remove_task(self, task_id):
        self.tasks.pop(task_id)
        return self.tasks

    # @classmethod
    # def view_tasks(cls): # this is a class method to show all tasks
    #     return f"all tasks : {cls.tasks}"

class ToDoList(Task):
    def __init__(self, task_id, task_name, task_description):
        super().__init__(task_id, task_name, task_description)

    def view_tasks(self):
        return f"all tasks : {Task.tasks}"

def todo_list():
    todo = ToDoList(0, "", "")
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            task_description = input("Enter the task description: ")
            todo = ToDoList(len(Task.tasks), task_name, task_description)
            todo.add_task()

        elif choice == "2":
            task_id = int(input("Enter the task ID to remove: "))
            todo.remove_task(task_id)

        elif choice == "3":
            print(todo.view_tasks())
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

todo_list()