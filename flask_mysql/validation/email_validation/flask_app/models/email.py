from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash
class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails"
        results = connectToMySQL('emails_schema').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL('emails_schema').query_db(query,data)

    @classmethod
    def validate_user(cls, data):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", 'email')
            is_valid = False
        query = "SELECT * FROM emails"
        results = connectToMySQL('emails_schema').query_db(query)
        for email_info in results:
            if cls(email_info).email == data['email']:
                flash("email is already taken")
                is_valid = False

        return is_valid

    
