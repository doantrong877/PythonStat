from crypt import methods
from flask import Flask, render_template, redirect,session, request
import random

app = Flask(__name__)
app.secret_key = "bimat"

@app.route('/')
def main():
    session.clear()
    session['attemp'] = 0
    session['admin'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess1',methods = ['POST'])
def guess1():
    session['input'] = int(request.form['input'])
    return redirect('/guess')

@app.route('/guess')
def guess():
    session['attemp'] += 1
    message = ""
    color =""
    correct = False
    if session['input'] < session['admin'] :
        message = "Too Low!"
        color = "red"
        correct = False
    elif session['input'] > session['admin'] :
        message = "Too High!"
        color = "red"
        correct = False
    else:
        message = "You Guessed It! The number was" + " "+ str(session['admin'])
        color = "green"
        correct = True
    return render_template('guess.html',message=message, color = color, correct = correct, attemp = session['attemp'])

@app.route('/finish',methods=['POST'])
def homedirect():
    return redirect('/')
if __name__ == "__main__":
    app.run(debug = True)