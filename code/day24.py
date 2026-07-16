# Day 24: Error Handling
# Goal: Prevent your program from crashing when something goes wrong.

# Concept: Use try and except blocks to handle exceptions gracefully.

# Day 24: Error Handling
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: You cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numbers only."
    else:
        return result
    finally:
        print("Operation attempt completed.")

print(divide_numbers(10, 0))