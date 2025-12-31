class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
        
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                return True
        return False

    def display_books(self):
        for book in self._books:
            print(f"{book.title} by {book.author} - {'Checked out' if book._is_checked_out else 'Available'}")

    def list_available_books(self):
        return [book for book in self._books if not book._is_checked_out]
