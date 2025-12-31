class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library():
    def __init__(self, books):
        self.books = []
        if books:
            for book in books:
                if isinstance(book, EBook):
                    self.books.append(EBook(book.title, book.author, book.file_size))
                elif isinstance(book, PrintBook):
                    self.books.append(PrintBook(book.title, book.author, book.page_count))
                else:
                    self.books.append(Book(book.title, book.author))

    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        for book in self.books:
            print(book)
    
