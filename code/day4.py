"""
Day 4: String Slicing and Methods
- Strings are immutable (cannot be changed once created).
"""

data = "  Python-Coding-Challenge  "

# Strip removes whitespace
clean_data = data.strip()

# Splitting creates a list
parts = clean_data.split("-")
print(f"Split data: {parts}")

# Advanced slicing [start:stop:step]
# Get the whole string in reverse
reversed_data = clean_data[::-1]
print(f"Reversed: {reversed_data}")