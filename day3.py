"""
Day 3: Operators
- Includes comparison, logical, and membership operators.
"""

x, y = 10, 20

# Comparison Operators
print(f"Is x greater than y? {x > y}")

# Membership Operator (very common in Python)
fruits = ["apple", "banana"]
print(f"Is apple in the list? {'apple' in fruits}")

# Logical Operators
if x < 20 and y > 10:
    print("Both conditions are met.")