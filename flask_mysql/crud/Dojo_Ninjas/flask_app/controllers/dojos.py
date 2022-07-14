from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route("/dojos")
def home():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)

@app.route("/dojos/<int:id>")
def dojo(id):
    data = {
        "id" : id
    }
    return render_template("dojo.html", dojo = Dojo.get_dojo_with_ninjas(data))

@app.route("/add/dojo", methods=['POST'])
def add_dojo():
    data={
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route("/ninja")
def ninja():

    return render_template("ninja.html", dojos = Dojo.get_all())