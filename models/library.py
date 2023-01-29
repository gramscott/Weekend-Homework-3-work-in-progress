from models.book import * 


book1 = Book("Into Deep", "Graeme Scott", "Thriller")
book2 = Book("Warrior of Scotland", "Sam McDaniels", "Action/Adventure")
book3 = Book("Don't Miss It", "Daisy Cope", "Comedy")
books = [book1, book2]


def add_new_book(book3):
    books.append(book3)

def remove_book():
    del books[0]


