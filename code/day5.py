"""
Day 5: Conditional Logic

What we learn today:
- How Python makes decisions using 'if', 'elif', and 'else'.
- The importance of Indentation (4 spaces) to define code blocks.
- Boolean logic (True/False evaluation).
"""

# Scenario: Checking access to a restricted area
age = 20
has_id = True

# We use 'if' to check the primary condition
if age >= 18:
    # Nested 'if' checks a secondary condition
    if has_id:
        print("Access Granted: You are an adult with valid ID.")
    else:
        print("Access Denied: ID required.")
        
# 'elif' handles alternative conditions
elif age >= 13:
    print("Access Denied: You are a teenager, not an adult.")

# 'else' is the catch-all for anything that doesn't meet the above
else:
    print("Access Denied: You are too young.")