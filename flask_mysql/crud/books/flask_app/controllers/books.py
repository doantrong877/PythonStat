from crypt import methods
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask import render_template, redirect, request

@app.route('/')
def home():
    return redirect("/books")

@app.route("/books")
def book():
    return render_template("books.html", books = Book.get_all())

@app.route("/add/book", methods = ['POST'])
def add_book():
    data = {
        "title" : request.form['name'],
        "num_of_pages" : request.form['pages']
    }
    Book.save(data)
    return redirect('/')

@app.route("/book/<int:id>")
def favo_author(id):
    data = {
        "id" : id
    }
    return render_template('favoriteauthor.html', book = Book.get_one(data), authors = Author.get_all(), favo = Book.get_book_with_authors(data))

@app.route("/add/favoauthor", methods=['POST'])
def add_favoauthor():
    data = {
        "first_name" : request.form['name']
        
    }
    
    book = request.form['book_id']
    Author.save(data)
    return redirect(f"/book/{book}")