class Library:
    def __init__(self):
        self.books_collection = {}
        self.members = {}

    def add_book(self, book, quantity=1):
        if book.title in self.books_collection:
            self.books_collection[book.title].copies_available += quantity
        else:
            self.books_collection[book.title] = book
        print(f"\nAdded {quantity} copies of '{book.title}' to the library 📚✅")

    def remove_book(self, book, quantity=1):
        if book.title in self.books_collection:
            if self.books_collection[book.title].copies_available > quantity:
                self.books_collection[book.title].copies_available -= quantity
                print(f"\nRemoved {quantity} copies of '{book.title}' from the library 📚❌")
            else:
                del self.books_collection[book.title]
                print(f"\nAll copies of '{book.title}' have been removed from the library 📚🚫")
        else:
            print(f"\n⚠️ The book '{book.title}' does not exist in the library!")

    def register_member(self, member):
        if member.member_id in self.members:
            print(f"\n⚠️ Member '{member.member_id}' is already registered!")
        else:
            self.members[member.member_id] = member
            print(f"\nRegistered {member.name} (member ID: {member.member_id}) as a member successfully 🆕✅")

    def lend_book(self, member_id, book_title):
        if member_id not in self.members:
            print(f"\n⚠️ Member ID '{member_id}' not found!")
            return

        if book_title not in self.books_collection:
            print(f"\nBook title '{book_title}' is not available in the library ❌")
            return

        member = self.members[member_id]
        book = self.books_collection[book_title]

        if book.is_available() and len(member.borrowed_books) < member.max_books_allowed:
            book.borrow_book(member)
            member.borrowed_books.append(book)

            if book.copies_available == 0:
                print(f"\nThe book '{book_title}' is now fully borrowed and has no available copies 📖❌")

            print(f"\n{member.name} (member ID: {member.member_id}) has successfully borrowed '{book_title}' ✅")

        else:
            print(f"\nSorry, '{book_title}' is not available for borrowing or member limit reached ⛔")

    def receive_book(self, member_id, book_title):
        if member_id not in self.members:
            print(f"\n⚠️ Member ID '{member_id}' not found!")
            return

        member = self.members[member_id]

        # Find the book in the member's borrowed list
        returned_book = None
        for book in member.borrowed_books:
            if book.title == book_title:
                returned_book = book
                break

        if returned_book is None:
            print(f"\nThe book '{book_title}' was not borrowed by {member.name} ❌")
            return

        # Return the book
        member.return_book(returned_book)

        # Restore the book in the library if it was removed
        if book_title not in self.books_collection:
            self.books_collection[book_title] = returned_book

        self.books_collection[book_title].copies_available += 1
        print(f"\nThe book '{book_title}' has been returned and is now available in the library 🔄✅")

    def search_book(self, title):
        if title in self.books_collection:
            book = self.books_collection[title]
            print(f"\nBook Found: '{book.title}' by {book.author} 🔍✅ | 📖 Copies Available: {book.copies_available}")
            return book
        else:
            print(f"\n⚠️ Book '{title}' not found in the library!")
            return None
