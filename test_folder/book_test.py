import unittest
from models.library import * 
from controllers.controller import *

class TestBook(unittest. TestCase):
    def setUp(self):
        self.title = "Into Deep"
        self.author = "Graeme Scott"
        self.genre = "Thriller"

        self.book1 = [self.title, self.author, self.genre]

    def test_book_has_title(self):
        self.assertEqual("Into Deep", self.title)

    def test_author_has_name(self):
        self.assertEqual("Graeme Scott", self.author)

    def test_book_has_genre(self):
        self.assertEqual("Thriller", self.genre)

    # def test_add_or_remove_book(self):
    #     add_new_book(self.books[-1])
    #     new_book = add_new_book(self.books)
    #     self.assertEqual(["The Bees Knees", "Gandalf", "Dramady"], new_book)


#         cash = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(1010, cash)
    
    
# def add_new_book(new_book):
#     books.append(new_book)

# def remove_book(book_to_remove):
#     books.remove(book_to_remove)

