from models.book import *


book1 = Book("Into Deep", "Graeme Scott", "Thriller")
book2 = Book("Warrior of Scotland", "Sam McDaniels", "Action/Adventure")
# book3 = Book["Text Back Plz", "Daisy Cope", "Comedy"]
books = [book1, book2]
book_to_remove = []

def add_new_book(new_book):
    books.append(new_book)

def remove_book(book_to_remove):
    books.remove(book_to_remove)
