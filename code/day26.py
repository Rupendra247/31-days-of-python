# Day 26: Decorators
# Goal: Add functionality to functions without changing their source code.

# Concept: A decorator is a function that takes another function as an argument and extends its behavior
# Day 26: Decorators
def logger(func):
    """Decorator that logs when a function is called."""
    def wrapper(*args, **kwargs):
        print(f"LOG: Calling function '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper

@logger
def say_hello(name):
    print(f"Hello, {name}!")

# When we call say_hello, it is now 'wrapped' by the logger
say_hello("Alice")