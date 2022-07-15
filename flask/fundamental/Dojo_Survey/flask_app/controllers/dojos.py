from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getInfo', methods=['POST'])
def info():
    if not Dojo.validate_dojo(request.form):

        return redirect('/')

    Dojo.save(request.form)
    

    return render_template('info.html', dojo = Dojo.get_one(request.form))

