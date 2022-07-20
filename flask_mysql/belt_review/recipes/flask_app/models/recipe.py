from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.under = data['under']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes"
        results = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    
    @classmethod
    def get_recipe_by_id(cls,data):
        query = "SELECT * FROM recipes WHERE recipes.id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes(user_id,name,description,instruction,created_at,updated_at,under) VALUES (%(user_id)s,%(name)s,%(description)s,%(instruction)s,%(created_at)s,NOW(),%(under)s);"
        return connectToMySQL('recipes_schema').query_db(query,data)

    @classmethod
    def validate_recipe(cls, data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters", "new_recipe")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters", "new_recipe")
            is_valid = False
        if len(data['instruction']) < 3:
            flash("name must be at least 3 characters", "new_recipe")
            is_valid = False
        if len(data['created_at']) < 1:
            flash("Date cannot be empty", "new_recipe")
            is_valid = False
        return is_valid

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE recipes.id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET user_id = %(user_id)s, name = %(name)s, description = %(description)s, instruction = %(instruction)s, created_at = %(created_at)s, under = %(under)s WHERE id = %(recipe_id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)