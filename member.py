class Member:
    def __init__(self, member_id, name, max_books_allowed=3):
        """
        Initializes a library member with an ID, name, and borrowing limit.
        """
        self.member_id = member_id  # Unique identifier for the member
        self.name = name  # Member's name
        self.borrowed_books = []  # List of borrowed books
        self.max_books_allowed = max_books_allowed  # Maximum books a member can borrow

    def borrow_book(self, book):
        """
        Allows the member to borrow a book if they haven't reached the borrowing limit 
        and the book is available.
        """
        if len(self.borrowed_books) >= self.max_books_allowed:
            print(f"\n⚠️ {self.name} (member ID: {self.member_id}) has reached the maximum borrowing limit of {self.max_books_allowed} books")
            return

        if book.is_available():
            self.borrowed_books.append(book)
            book.copies_available -= 1
            print(f"\n{self.name} (member ID: {self.member_id}) has successfully borrowed '{book.title}' ✅")
        else:
            print(f"\nSorry, '{book.title}' is currently unavailable ❌")

    def return_book(self, book):
        """
        Allows the member to return a borrowed book and updates availability in the library.
        """
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            book.copies_available += 1
            print(f"\n{self.name} (member ID: {self.member_id}) has successfully returned '{book.title}' 🔄✅")
            return True
        else:
            print(f"\n⚠️ {self.name} (member ID: {self.member_id}) did not borrow '{book.title}'")
            return False

    def view_borrowed_books(self):
        """
        Displays a list of books currently borrowed by the member.
        """
        if not self.borrowed_books:
            print(f"\n📭 {self.name} (member ID: {self.member_id}) has not borrowed any books")
        else:
            print(f"\n📚 Books that {self.name} (member ID: {self.member_id}) has borrowed:")
            for book in self.borrowed_books:
                print(f"📖 {book.title} by {book.author}")
