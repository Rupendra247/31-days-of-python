# Day 31: Implementation & Persistence (main.py)
# Goal: Make it "real world" with data persistence and error handling.

# Concept: Save data to a JSON file so it persists even after the script ends.
"""
Day 31: Advanced Persistence and Final Integration
Concept: Using JSON for data storage and 'try-except' for robust file handling.



"""
from day30 import TaskManager
import json
import logging

# Configure logging (Day 29 concept)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class AdvancedTaskManager(TaskManager):
    def save_to_file(self):
        try:
            with open(self.filename, 'w') as f:
                # Use list comprehension (Day 25) to map tasks to dicts
                data = [t.to_dict() for t in self.tasks]
                json.dump(data, f)
            logging.info("Tasks saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save: {e}")

if __name__ == "__main__":
    app = AdvancedTaskManager()
    app.add_task("Finish 31 Days of Python", "Celebrate the milestone!")
    app.save_to_file()