# Introduction
# Day 1 - 31DaysOfPython Challenge
"""
Day 1: Introduction to Python
- Python is an interpreted language.
- The 'print()' function is the primary way to output data.
"""

# Standard output
print("Hello, World!") 

# Printing multiple items with a separator
print("Python", "is", "awesome", sep="-")

# Using the end parameter to stay on the same line
print("Loading", end="...")
print("Done!")


print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name': 'Asabeneh'}))  # Dictionary
print(type({9.8, 3.14, 2.7}))    # Tuple
print(type({'name': 'Rupendra',
            "id" :"20001"
            }))  # Dictionary