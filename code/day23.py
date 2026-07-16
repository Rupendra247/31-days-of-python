"""
Day 23: Library Management System
Concept: This combines everything we learned. 
1. Encapsulation: Hiding internal state (__is_checked_out).
2. Inheritance: Creating specific books from a general 'Book' class.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Encapsulation: We add double underscores to make this 
        # attribute 'private' so it cannot be changed from outside.
        self.__is_checked_out = False 

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            print(f"Success: '{self.title}' has been checked out.")
        else:
            print(f"Error: '{self.title}' is already checked out.")

class Library:
    def __init__(self):
        # We store our book objects here
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"System: Added '{book.title}' to the library catalog.")

if __name__ == "__main__":
    # Creating the system
    my_library = Library()
    
    # Adding a book
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    my_library.add_book(book1)
    
    # Testing our encapsulated logic
    book1.check_out()
    book1.check_out() # This will trigger our error message