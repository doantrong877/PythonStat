from crypt import methods
from email import message
from flask import Flask, render_template, redirect, session, request
import random
from datetime import datetime


app = Flask(__name__)
app.secret_key = "bimat"

@app.route('/')
def home():
    session['gold'] = 0
    session['message'] = ""
    return render_template("index.html")

@app.route('/process', methods = ['POST'])
def process():
    now = datetime.now()
    session['time'] = now.strftime("%d/%m/%Y %H:%M:%S")
    session['building'] = request.form['building']
    return redirect("/process_money")

@app.route("/process_money")
def process_money():
    if session['building'] == "farm":
        num = random.randint(10,20)
        session['gold'] += num
        session['message'] += f"<p>Earned {num} golds from the farm! ({session['time']}) </p>"

    elif session['building'] == "cave":
        num = random.randint(5,10)
        session['gold'] += num
        session['message'] += f"<p>Earned {num} golds from the cave! ({session['time']}) </p>"
    
    elif session['building'] == "house":
        num = random.randint(2,5)
        session['gold'] += num
        session['message'] += f"<p>Earned {num} golds from the house! ({session['time']}) </p>"

    elif session['building'] == "casino":
        choice = random.randint(0,1)
        num =  random.randint(0,50)
        if choice == 0:
            session['gold'] += num
            session['message'] += f"<p>Enter a casino and earned {num} golds! ({session['time']}) </p>"
        else:
            session['gold'] -= num
            session['message'] += f"<p>Enter a casino and lost {num} golds... Ouch.. ({session['time']}) </p>"
    return render_template("process.html", message=session['message'], gold =session['gold'])

if __name__ == '__main__':
    app.run(debug=True)