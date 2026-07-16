"""
Day 22: Magic (Dunder) Methods
Concept: Magic methods (starting and ending with __) allow your 
custom classes to work with Python's built-in syntax like 
print(), +, len(), etc.
"""

class ShoppingCart:
    def __init__(self):
        # Initializing an empty list to hold items
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        """
        __str__ defines what happens when you call print(my_object).
        Without this, print() would just show a memory address.
        """
        return f"Cart with {len(self.items)} items: {', '.join(self.items)}"

    def __add__(self, other):
        """
        __add__ allows us to use the '+' operator.
        We create a new cart that combines items from two existing carts.
        """
        new_cart = ShoppingCart()
        new_cart.items = self.items + other.items
        return new_cart

if __name__ == "__main__":
    c1 = ShoppingCart()
    c1.add_item("Laptop")
    
    c2 = ShoppingCart()
    c2.add_item("Mouse")
    
    # Using our custom '+' operator logic
    combined = c1 + c2 
    print(combined) # Uses our __str__ method to display the result