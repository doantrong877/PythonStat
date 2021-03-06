from pydoc import describe
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask import flash, render_template, session, redirect, request

#add recipe
@app.route('/recipes/new')
def add_recipe():
    return render_template('new_recipe.html')

#save recipe
@app.route('/addrecipe', methods = ['POST'])
def save_recipe():
    if not Recipe.validate_recipe(request.form):
        if  'box' not in request.form :
            flash("please check cook time",'new_recipe')
        return redirect('/recipes/new')
    data = {
        'user_id' : session['user_id'],
        'name' : request.form['name'],
        'description': request.form['description'],
        'instruction': request.form['instruction'],
        'created_at' : request.form['created_at'],
        'under' : request.form['box']
    }
    Recipe.save(data)
    return redirect('/recipes')

#get recipe info
@app.route('/recipes/<int:id>')
def get_recipe_info(id):
    user_data ={
        'id' : session['user_id']
    }
    recipe_data = {
        'id' : id
    }
    
    recipe = Recipe.get_recipe_by_id(recipe_data)
    poster = {
        'id': recipe.user_id
    }
    return render_template('recipe_info.html', user_name = User.get_one(user_data).first_name, name = recipe.name,
                    description = recipe.description, under = recipe.under, instruction = recipe.instruction, date_made= recipe.created_at, poster =  User.get_one(poster).first_name )

#delete recipe
@app.route('/delete/<int:id>')
def delete_recipe(id):
    data = {
        'id' : id
    }
    Recipe.destroy(data)
    return redirect('/recipes')

#edit recipe
@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    recipe_data = {
        'id' : id
    }
    recipe = Recipe.get_recipe_by_id(recipe_data)
    session['recipe_id'] = id
    return render_template('edit_recipe.html', name = recipe.name, description = recipe.description, instruction = recipe.instruction, under = recipe.under)

#get data from edit
@app.route('/edit/recipe', methods=['POST'])
def edit():
    if not Recipe.validate_recipe(request.form):
        id = session['recipe_id']
        if  'box' not in request.form :
            flash("please check cook time",'new_recipe')
        return redirect(f'/recipes/edit/{id}')
    data = {
        'user_id' : session['user_id'],
        'name' : request.form['name'],
        'description': request.form['description'],
        'instruction': request.form['instruction'],
        'created_at' : request.form['created_at'],
        'under' : request.form['box'],
        'recipe_id' : session['recipe_id']
    }
    Recipe.update(data)
    return redirect('/recipes')