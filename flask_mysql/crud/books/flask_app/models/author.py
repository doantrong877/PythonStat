from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (name, num_of_pages, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('book_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_author_with_books(cls, data):
        query = "SELECT * FROM users LEFT JOIN favorites ON users.id = favorites.book_id LEFT JOIN books ON favorites.user_id = books.id WEHRE users.id = %(id)s; "
        result = connectToMySQL("books.schema").query_db(query,data)
        authors = cls(result[0])
        for author in result:
            book_data = {
                "id" : author['books.id'],
                "title": author['title'],
                "num_of_pages" : author['num_of_pages'],
                "created_at" : "NOW()",
                "updated_at" : "NOW()"
            }
        authors.books.append(book.Book(book_data))
        return authors

            




