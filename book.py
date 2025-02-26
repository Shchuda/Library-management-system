class Book:
    def __init__(self, title, author, ISBN, copies_available):
        """
        Initializes a book with title, author, ISBN, and available copies.
        """
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies_available = copies_available

    def is_available(self):
        """
        Checks if the book is available for borrowing.
        Returns True if at least one copy is available, otherwise False.
        """
        return self.copies_available > 0

    def borrow_book(self, member):
        """
        Allows a member to borrow the book if copies are available.
        Reduces available copies by 1 if successful.
        """
        if self.is_available():
            self.copies_available -= 1
            print(f"\n{member.name} (member ID: {member.member_id}) has borrowed the book '{self.title}' ✅")
            return True
        else:
            print(f"\nSorry, the book '{self.title}' cannot be borrowed. All copies have been borrowed ❌")
            return False

    def return_book(self):
        """
        Allows a member to return the book.
        Increases available copies by 1 upon return.
        """
        self.copies_available += 1
        print(f"\nYou have returned the book '{self.title}' 🔄✅")
        return True
