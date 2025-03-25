import random

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    
    def update_stock(self, quantity):
        if quantity > self.stock:
            return f"Not enough stock.Available stock is: {self.stock}"
            
        else:
            self.stock -= quantity
            return f"Stock updated.New stock is: {self.stock}"
        
    def get_info(self):
        return f"Title: {self.title}. Author: {self.author}. Price: {self.price}"
    
    def apply_discount(self, discount_percent: int):
        return self.price - (self.price * discount_percent / 100)
    

class Library(Book):
    def __init__(self):
        self.books = []
        
    
    def add_book(self, book):
        return self.books.append(book)
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return f"{book.title} has been removed from the library"
        else:
            return "Book not found in the library"
        
    def calculate_total_value(self):
        total_value = sum(book.price * book.stock for book in self.books)
        return total_value
    
    def show_books(self):
        if not self.books:
            return "No books available in the library."
        book_details = "Books in Library:\n"
        for book in self.books:
            book_details += f"Title: {book.title}, Author: {book.author}, Price: {book.price}, Stock: {book.stock}\n"
        return book_details



book1 = Book("Python Programming", "John Doe", 39.99, 10)
book2 = Book("Data Science with Python", "Jane Doe", 49.99, 5)

library = Library()
library.add_book(book1)
library.add_book(book2)

print(library.show_books())
print(f"Total Value of Books: {library.calculate_total_value()}")

book1.update_stock(2)
library.remove_book(book2)
print(library.show_books())
print(f"Total Value of Books after removal: {library.calculate_total_value()}")