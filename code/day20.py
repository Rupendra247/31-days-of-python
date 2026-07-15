# Day 20: Polymorphism
# Goal: Achieve "Many Forms" with one interface.

# Concept: Polymorphism allows different classes to be treated as instances of the same general class through the same method names (e.g., calling .speak() on both a Dog and a Cat).

# Day 20: Polymorphism
from day18 import Cat , Dog

def animal_sound(animal):
    # This function doesn't care WHAT the animal is,
    # as long as it has a .speak() method.
    animal.speak()

dog = Dog()
cat = Cat()

# We call the same function on different objects
animal_sound(dog) # Dog barks
animal_sound(cat) # Cat meows