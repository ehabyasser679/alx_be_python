class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self._file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self._page_count = page_count

class library:
    def __init__(self,books):
        self._books = []
        for book in books:
            if isinstance(book, EBook):
                self._books.append(EBook(book.title, book.author, book._file_size))
            elif isinstance(book, PrintBook):
                self._books.append(PrintBook(book.title, book.author, book._page_count))
            else:
                self._books.append(Book(book.title, book.author))

    def add_book(self, book):
        self._books.append(book)
    def list_books(self):
        for book in self._books:
            print(book)
    
