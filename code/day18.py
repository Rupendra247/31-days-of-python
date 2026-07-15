# Goal: Reuse code across different classes.

# Concept: Inheritance allows a "Child" class to inherit all attributes and methods from a "Parent" class, but also add its own unique features.
# Day 18: Inheritance
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal): # Dog inherits from Animal
    def speak(self): # Overriding the parent method
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

my_dog = Dog()
my_dog.speak() # Output: Dog barks