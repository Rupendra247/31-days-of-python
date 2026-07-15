# Day 25: List/Dict Comprehensions
# Goal: Write concise, readable code.

# Concept: Comprehensions allow you to create new lists or dictionaries from existing ones in a single line

# Day 25: Comprehensions
numbers = [1, 2, 3, 4, 5, 6]

# List Comprehension: [expression for item in iterable if condition]
even_squares = [x**2 for x in numbers if x % 2 == 0]

# Dict Comprehension: {key: value for item in iterable}
square_dict = {x: x**2 for x in numbers}

print(f"Even squares: {even_squares}")
print(f"Square dict: {square_dict}")