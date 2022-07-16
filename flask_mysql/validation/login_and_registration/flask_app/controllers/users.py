from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    if request.form['password'] != request.form['confirm_password']:
        flash("passwords doesn't match", 'register') 
        return redirect('/')
    if not User.validate_registration(request.form):       
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data =  {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        'password' : pw_hash
    }
    user = User.save(data)
    session ['user_info'] = f"{request.form['first_name']} {request.form['last_name']}"
    session['email'] = request.form['email']
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = {'email': request.form['email']}
    user = User.get_by_email(data)
    if not user :
        flash("Email has not been registed","login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect('/')
    session['user_id'] = user.id
    session ['user_info'] = f"{user.first_name} {user.last_name}"
    return redirect('/dashboard')
    

@app.route('/dashboard')
def dashboard():

    return render_template('logout.html', userinfo = session['user_info'])

@app.route('/logout')
def logout():
    session.clear
    return redirect('/')

