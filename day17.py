# Day 17: Methods & Attributes
# Goal: Manage object state and behavior.

# Concept: Attributes store data (what the object is), and Methods perform logic (what the object does). The self parameter is how an object refers to its own data
# Day 17: Attributes vs Methods
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner     # Instance attribute
        self.balance = balance # Instance attribute

    def deposit(self, amount): # Instance method
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)