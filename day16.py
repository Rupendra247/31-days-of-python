# Day 16: Introduction to OOP (Classes & Objects)
# Goal: Transition to Object-Oriented Programming (OOP).

# Concept: OOP lets you model real-world things. A Class is a blueprint, and an Object is the specific instance created from that blueprint.

# Day 16: Classes and Objects
class Car:
    # The __init__ method is a constructor; it sets up initial attributes
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def display_info(self): # Method
        print(f"Car: {self.brand} {self.model}")

# Creating instances (objects) of the class
my_car = Car("Toyota", "Corolla")
your_car = Car("Tesla", "Model 3")

my_car.display_info()
your_car.display_info()