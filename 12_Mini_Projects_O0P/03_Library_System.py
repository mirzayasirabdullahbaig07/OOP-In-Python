"""
Project: Library System
Category: Core Concepts (OOP)
Description: 
A simple Library Management System to manage books. Users can borrow and return books.
This project demonstrates core OOP concepts: classes, objects, methods, and encapsulation.

OOP Concepts Demonstrated:
1. Classes & Objects:
   - Book: Represents a single book.
   - Library: Represents a collection of books.
   - Each book created is an object of the Book class.
2. Encapsulation:
   - The 'is_borrowed' attribute is managed via borrow_book and return_book methods.
   - Users cannot directly change the borrowed status without using methods.
3. Methods:
   - add_book, show_books, borrow_book, return_book encapsulate functionality for reusability.
4. Abstraction:
   - Users interact with the library via methods without knowing internal data structure.
5. Inheritance / Polymorphism:
   - Not used here, but can be added if we create specialized types of books or users.

Example Run:

=== Library Menu ===
1. Show all books
2. Borrow a book
3. Return a book
4. Add a book
5. Exit
Enter your choice (1-5): 1

Library Books:
1. The Alchemist by Paulo Coelho - Available
2. 1984 by George Orwell - Available
3. Python Programming by John Zelle - Available

Enter your choice (1-5): 2
Enter the title of the book to borrow: 1984
You have borrowed '1984'. Enjoy reading!

Enter your choice (1-5): 1

Library Books:
1. The Alchemist by Paulo Coelho - Available
2. 1984 by George Orwell - Borrowed
3. Python Programming by John Zelle - Available
"""

# ------------------------
# Class Definitions
# ------------------------

class Book:
    """Represents a book in the library (Class & Object Concept)"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Encapsulation: controlled by methods

    def __str__(self):
        """Return the string representation of the book"""
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    """Represents the library containing books (Class & Object Concept)"""
    def __init__(self):
        self.books = []  # Stores book objects

    def add_book(self, book):
        """Add a book to the library (Method & Encapsulation)"""
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def show_books(self):
        """Display all books (Method & Abstraction)"""
        if not self.books:
            print("Library is empty.")
            return
        print("\nLibrary Books:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book}")
        print()

    def borrow_book(self, title):
        """Borrow a book if available (Encapsulation & Method)"""
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You have borrowed '{book.title}'. Enjoy reading!")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Return a borrowed book (Encapsulation & Method)"""
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Thank you for returning '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' was not borrowed.")
                    return
        print(f"Book '{title}' not found in the library.")


# ------------------------
# Main Program
# ------------------------

def main():
    library = Library()  # Object of Library class

    # Pre-populate library with some books (Objects of Book class)
    library.add_book(Book("The Alchemist", "Paulo Coelho"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("Python Programming", "John Zelle"))

    while True:
        print("\n=== Library Menu ===")
        print("1. Show all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Add a book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library.show_books()
        elif choice == "2":
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)
        elif choice == "3":
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        elif choice == "4":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            library.add_book(Book(title, author))
        elif choice == "5":
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")


if __name__ == "__main__":
    main()
