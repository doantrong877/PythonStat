from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.email import Email


@app.route('/')
def home():
    return render_template('email.html')

@app.route('/getinfo', methods=['POST'])
def get_info():
    if not Email.validate_user(request.form):
        return redirect('/')
    
    Email.save(request.form)
    return redirect("/display")


@app.route('/display')
def display():
    emails = Email.get_all()
    return render_template('info.html', emails=emails)

