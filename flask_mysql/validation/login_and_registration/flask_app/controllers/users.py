from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     



app.route('/')
def home():
    return render_template('login.html')

app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    User.save(request.form)

    userinfo = User.get_by_email(request.form['email'])

    

    return render_template('logout.html', userinfo = userinfo)
