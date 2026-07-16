# Day 13: Lambda Functions & Higher-Order Functions
# Goal: Learn "Anonymous" functions and functional programming tools.

# Concept: - Lambda: A small, one-line function.

# map(), filter(), reduce(): Tools to process collections without writing explicit loops.


# Day 13: Lambda and Functional Tools

# A normal function vs a lambda function
# Normal: def square(x): return x * x
square = lambda x: x * x 

numbers = [1, 2, 3, 4, 5]

# map(): applies a function to every item in the list
squared_numbers = list(map(lambda x: x**2, numbers))

# filter(): keeps only items where the condition is True
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Squared: {squared_numbers}")
print(f"Evens: {evens}")

# Use lambda when you need a simple function for a short period,
# typically passed as an argument to another function.

scores = [45, 88, 32, 95, 70]

# Keep only passing scores (50 or higher)
passing_scores = list(filter(lambda score: score >= 50, scores))

print(passing_scores)
# Output: [88, 95, 70]