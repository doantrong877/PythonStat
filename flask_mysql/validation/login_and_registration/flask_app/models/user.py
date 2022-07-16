from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s,NOW(), NOW());"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def validate_registration(cls, data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash("First name has two have at least 2 character",'register')
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name has two have at least 2 character",'register')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email addess!",'register')
            is_valid = False
        if len(data['password']) < 8:
            flash("Password need at least 8 characters",'register')
            is_valid = False
        if  cls.get_by_email(data) != False:
            flash("email has already registed",'register')
            is_valid = False
        return is_valid
    
    