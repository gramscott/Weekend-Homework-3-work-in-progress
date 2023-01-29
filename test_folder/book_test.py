import unittest 
from models.library import * 
from controllers.controller import *


class TestBook(unittest. TestCase):
    def setUp(self):
        self.title = "Into Deep"
        self.author = "Graeme Scott"
        self.genre = "Thriller"

    def test_book_has_title(self):
        self.assertEqual("Into Deep", self.title)

    def test_author_has_name(self):
        self.assertEqual("Graeme Scott", self.author)

    def test_book_has_genre(self):
        self.assertEqual("Thriller", self.genre)
