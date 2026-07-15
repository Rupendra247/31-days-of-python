# Day 30: Designing the Project (task_manager.py)
# Goal: Structure the application using OOP.

# Concept: We will encapsulate our tasks in a Task class and manage them with a TaskManager class.

"""
Day 30: Task Manager Architecture
Concept: A class-based structure makes the application modular 
and easy to extend in the future.
"""
import json

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def to_dict(self):
        # Convert object to dict for JSON serialization
        return {"title": self.title, "desc": self.description, "done": self.completed}

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []

    def add_task(self, title, desc):
        new_task = Task(title, desc)
        self.tasks.append(new_task)
        print(f"Task '{title}' added.")