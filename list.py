class Task:
    def __init__(self, task_id, task_name):
        self.task_id = task_id
        self.task_name = task_name


class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        if task is not None:
            self.task_list.append(task)
        else:
            raise ValueError("Task is empty")

    def remove_task_by_id(self, task_id):
        if task_id is None:
            raise ValueError("Task id can not be empty")

        for task in self.task_list:
            if task.task_id == task_id:
                self.task_list.remove(task)
                print(f"Task ID - {task_id} has been removed from the list")
                return

    def show_tasks(self):
        if len(self.task_list) > 0:
            for task in self.task_list:
                print(f"TaskID - {task.task_id} and TaskName - {task.task_name}")


# client
task1 = Task(1, "Prepare the document and submit to CEO")
task2 = Task(2, "Complete the database architecture of a new game")

task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)

task_manager.show_tasks()

task_manager.remove_task_by_id(1)

task_manager.show_tasks()
