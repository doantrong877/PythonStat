from flask import Flask, render_template, redirect, session, request

from user import User


app = Flask(__name__)
app.secret_key = "bimat"

@app.route("/users")
def index():
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
        'email' : request.form['email'],
            }

    User.save(data)
   
    return redirect('/users')




if __name__ == "__main__":
    app.run(debug=True)