class Task():
    def __init__(self, description):
        self.description = description
        self.completed = "Not Completed" 
        
    def mark_completed(self):
        self.completed = "Completed"

class ToDoList():
    def __init__(self):
        self.tasks = {}
        
    def add_task(self, description):
        task = Task(description)
        self.tasks[description] = 
        