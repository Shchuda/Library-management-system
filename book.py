class Book:
    def __init__(self, title, author, ISBN, copies_available):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies_available = copies_available

    def is_available(self):
        return self.copies_available > 0

    def borrow_book(self, member):
        if self.is_available():
            self.copies_available -= 1
            print(f"\n{member.name} (member ID: {member.member_id}) has borrowed the book '{self.title}' ✅")
            return True
        else:
            print(f"\nSorry, the book '{self.title}' cannot be borrowed. All copies have been borrowed ❌")
            return False

    def return_book(self):
        self.copies_available += 1
        print(f"\nYou have returned the book '{self.title}' 🔄✅")
        return True
