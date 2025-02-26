from library import Library  # Import your Library class
from book import Book  # Import your Book class
from member import Member  # Import your Member class

# Create the library
library = Library()

# Create some books
book1 = Book("Python Programming", "John Doe", "12345", 3)
book2 = Book("Data Structures", "Jane Smith", "67890", 2)
book3 = Book("Cooking", "Jane Tom", "67891", 2)

# Add books to the library
library.add_book(book1, 3)
library.add_book(book2, 2)

# Register members
member1 = Member(101, "Alice")
member2 = Member(102, "Bob")

library.register_member(member1)
library.register_member(member2)

# Search for books
library.search_book("Python Programming")
library.search_book("Data Structures")

# Member borrows a book
library.lend_book(101, "Python Programming")  # Alice borrows Python book
library.lend_book(102, "Data Structures")  # Bob borrows Data Structures book

member2.borrow_book(book3)
member2.borrow_book(book3)
member2.borrow_book(book3)

# View borrowed books
member1.view_borrowed_books()
member2.view_borrowed_books()

# Member tries to borrow the same book again (should fail if copies are zero)
library.lend_book(101, "Python Programming")

# Member returns a book
library.receive_book(101, "Python Programming")

# Check if the book is now available again
library.search_book("Python Programming")
