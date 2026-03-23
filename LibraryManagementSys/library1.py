# Library Management System

"""
In this video (0:00), the user is tasked with creating a Library Management System 
in Python using Object-Oriented Programming. Specifically, you need to create a Library class 
with the following requirements:

Required Variables:
no_of_books: An integer representing the count of books (0:34).
books: A list to store the book titles (0:37).
Required Methods:
Methods to add books to the library (0:46).
A method to display available books (0:46).
A method to check the number of books and ensure it matches the length of the list (1:02).
Additionally, you can create multiple library objects (e.g., library1, library2) (1:15).

Final Challenge: The video asks to determine if the books you add persist in memory after the program stops (1:21).
"""

class Library:
    def __init__(self, books):
        self.books = books[:] # copy List to avoid shared reference
        self.no_of_books = len(books)

    def addBook(self, newBook):
        self.books.append(newBook)
        self.no_of_books += 1

    def displayBook(self):
        print("Available Books: ")
        for book in self.books:
            print(book)

    def check_num(self):
        if len(self.books) == self.no_of_books:
            print("Count is correct")
        else:
            print("Count mismatch")

book_List = ["M1", "M2", "M3", "M4", "M5", "ADA", "SA"]

# Create object

library1 = Library(book_List)

library1.displayBook()

library1.addBook("Discrete")

print("\nAfter Adding Book: ")
library1.displayBook()