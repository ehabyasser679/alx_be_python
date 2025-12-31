class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__ (self, title, author, year):
        return f"title {self.title}", f"by {self.author}", "published in {self.year}"
    
    def __repr__ (self, title, author, year):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def __del__ (self,title):
        print(f"Deleting ({self.title})")
