from project.task import Task

class Section:
    def __init__(self,name :str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self,new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self,task_name: str):
        is_located = ((t for t in self.tasks if t.name == task_name),None)

        if is_located:
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        tasks = len(self.tasks)
        self.tasks.clear()
        return f"Cleared {tasks} tasks."

    def view_section(self):
        section_tasks = []
        for task in self.tasks:
            section_tasks.append(task.details())

        return '\n'.join(section_tasks)




