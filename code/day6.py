"""
Day 6: While Loops
- Use when the number of iterations is unknown.
"""

balance = 100
while balance > 0:
    print(f"Remaining Balance: ${balance}")
    balance -= 20
    
    if balance == 40:
        print("Warning: Low balance!")
        break # Exits the loop entirely