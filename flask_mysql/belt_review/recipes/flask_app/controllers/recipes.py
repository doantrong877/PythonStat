from flask_app import app
from flask_app.models.recipe import Recipe
from flask import flash, render_template, session, redirect, request

#add recipe
@app.route('/recipes/new')
def add_recipe():
    return render_template('new_recipe.html')

#save recipe
@app.route('/addrecipe', methods = ['POST'])
def save_recipe():
    if not Recipe.validate_recipe(request.form):
        print(request.form)
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
    session['recipe_id'] = Recipe.save(data)
    return redirect('/recipes')