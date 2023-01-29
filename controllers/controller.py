from flask import render_template, request
from app import app 
from models.library import *
from models.book import Book







@app.route("/books")
def index():
    return render_template("index.html", title="BOOKS ARE CLASS!", books=books)















@app.route("/books<int:id>")
def the_chosen_one(id):
    return render_template("book.html", title="Your Book", book=books[id])






@app.route("/add_book", methods=["POST"])
def add_book():
    add_new_book(book3)
    return render_template("index.html", title="BOOKS ARE CLASS!", books=books(book3))


@app.route("/remove_book", methods=["POST"])
def remove_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    remove_books = Book(title, author, genre)
    remove_book(remove_books)
    return render_template("index.html", title="Home", books=books[0])
