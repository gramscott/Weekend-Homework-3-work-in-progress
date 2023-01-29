from flask import render_template, request
from app import app
from models.book import Book
from models.library import *


@app.route('/books')
def index():
    return render_template("index.html", title="Good Books", books=books)


@app.route('/books/<int:id>')
def get_a_book(id):
    return render_template("book.html", title="Good Books", book=books[id])


@app.route('/library', methods=['POST'])
def new_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book) 
    return render_template("index.html", title="Good Book", books=books)


@app.route('/remove', methods=['POST'])
def remove_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    book_to_remove = Book(book_title, book_author, book_genre)
    remove_book(book_to_remove) 
    return render_template("index.html", title="Good Book", books=books)

