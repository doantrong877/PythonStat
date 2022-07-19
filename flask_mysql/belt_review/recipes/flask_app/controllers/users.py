from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#load home page
@app.route('/')
def home():
    return render_template('home.html')

#register route
@app.route('/register', methods=['POST'])
def register():

    #check for invalid input
    if not User.validate_registration(request.form):
        return redirect('/')
    
    
    #check matching password
    if request.form['password'] != request.form['confirm_password']:
        flash("Passwords don't match", 'register')
        return redirect('/')

    #hash password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
    #put hash password into data
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash
    }
   
    #assign session id
    session['user_id'] = User.save(data)
    

    return redirect('/recipes')

#Welcome page

@app.route('/recipes')
def welcome_page():
    data ={
        'id' : session['user_id']
    }
    return render_template('welcome_page.html', name = User.get_one(data).first_name)


#logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')