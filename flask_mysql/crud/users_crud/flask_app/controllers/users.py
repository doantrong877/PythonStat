from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User
@app.route("/")
def index():
    users = User.get_all()
    return redirect('/users')

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("read.html", users = users)

@app.route('/user/new')
def create():
    return render_template("create.html")

@app.route('/create', methods =['POST'])
def user_input():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email']
            }

    User.save(data)
   
    return redirect('/users')

@app.route('/delete/<int:id>')
def delete_user(id):
    data = {"id" : id}
    User.delete(data)
    return redirect("/users")

@app.route('/show/<int:id>')
def display_user(id):
    data = {"id" : id}
    user = User.get_user(data)
    return render_template('info.html', user = user)

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id" : id
    }
    user = User.get_user(data)
    return render_template('edit.html', user = user)


@app.route('/update', methods =['POST'])
def update():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email'],
            }

    User.edit(data)
   
    return redirect('/users')