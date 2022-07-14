from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja



@app.route("/add/ninja", methods = ["POST"])
def add_ninja():
    data ={
        "fname" : request.form['fname'],
        "lname": request.form['lname'],
        "age": request.form['age'],
        "dojo_id": request.form['location']
    }
    Ninja.save(data)
    return redirect('/')