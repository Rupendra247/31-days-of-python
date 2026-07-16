# Day 11: Functions Part 1 (Defining & Returning)
# Goal: Learn how to bundle code into reusable blocks.

# Concept: A function is a named section of code that performs a specific task. We use def to define them and return to send data back.

# Python

# Day 11: Defining Functions
def calculate_area(radius):
    """
    Calculates the area of a circle.
    This docstring explains what the function does.
    """
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

# Calling the function
result = calculate_area(5)
print(f"The area of the circle is: {result:.2f}")

# Functions improve readability and prevent code duplication (DRY principle)