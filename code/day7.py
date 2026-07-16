"""
Day 7: For Loops

What we learn today:
- The 'for' loop is used for iterating over sequences (lists, strings, ranges).
- The 'enumerate()' function helps get both the index and the value.
- 'range()' allows us to control how many times a loop runs.
"""

# A list of items to process
tasks = ["Write code", "Document code", "Push to GitHub"]

# Basic loop: Processing each item
print("To-Do List ")
for task in tasks:
    print(f"Task: {task}")

# Using 'enumerate' to get the current position (index)
# This is useful when you need to know the 'step' number
print("\n Indexed Steps ")
for index, task in enumerate(tasks, start=1):
    print(f"Step {index}: {task}")

# Using 'range' for repetition (e.g., repeating an action 3 times)
print("\n Repetition ")
for i in range(3):
    print(f"Loop cycle: {i+1}")