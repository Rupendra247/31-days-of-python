# Day 12: Functions Part 2 (Arguments & Scope)
# Goal: Master dynamic arguments and understand variable visibility.

# Concept: - *args: Allows a function to accept any number of positional arguments.

# kwargs: Allows a function to accept any number of keyword (named) arguments.

# Scope: Variables defined inside a function don't exist outside it.

# Day 12: Flexible Arguments and Scope
def display_user_info(username, *hobbies, **details):
    # *hobbies becomes a tuple, **details becomes a dictionary
    print(f"User: {username}")
    
    print("Hobbies:")
    for hobby in hobbies:
        print(f"- {hobby}")
        
    print("Additional Info:")
    for key, value in details.items():
        print(f"{key}: {value}")

# Using the function
display_user_info("Alice", "Reading", "Cycling", city="New York", status="Active")