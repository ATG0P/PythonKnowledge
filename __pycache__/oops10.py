class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def diplay_books(self):
        return [f"{book.title} by {book.author}"for book in self.books]
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
library = Library("Mumbai Public Library")
b1 = Book("Harry Potter","J.K Rowling")
b2 = Book("Atomic Habits","James Clear")
b3 = Book("The Monk Who Sold His Ferrari","Robin Sharma")
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
print(library.name)
print(library.diplay_books()) 