# 31 Days of Python: Phase 2 - Data Structures (Days 8-10)

## 📅 Day 8: Lists
# **Goal:** Manage ordered, mutable collections of items.
# **Concept:** Lists are the "workhorse" of Python. You can store any data type, even a mix of types, in a single list.


# Day 8: Lists - Deep Dive
# Lists are mutable, meaning we can change them after creation.

# Creation
shopping_cart = ["Apples", "Milk", "Bread"]

# Adding items
shopping_cart.append("Eggs")      # Adds to the end
shopping_cart.insert(1, "Juice")  # Adds at a specific index

# Removing items
shopping_cart.remove("Milk")      # Removes by value
popped_item = shopping_cart.pop() # Removes and returns the last item

# List Comprehensions: A very "Pythonic" way to create lists
# Example: Create a list of squares for numbers 0-9
squares = [x**2 for x in range(10)]

print(f"Final Cart: {shopping_cart}")
print(f"Squares list: {squares}")