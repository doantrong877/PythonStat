from flask_app import app
from flask_app.models.book import Book
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