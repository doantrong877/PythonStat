from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES ( %(title)s, %(num_of_pages)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        result = connectToMySQL('books_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_book_with_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN users ON favorites.user_id = users.id WHERE books.id = %(id)s; "
        result = connectToMySQL("books_schema").query_db(query,data)
        books = cls(result[0])
        for book in result:
            author_data = {
                "id" : book['users.id'],
                "first_name": book['first_name'],
                "created_at" : "NOW()",
                "updated_at" : "NOW()"
            }
            books.authors.append(author.Author(author_data))
        return books

            




