from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)  
app.secret_key ="bimat"
@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    now = datetime.now()
    session['time'] = now.strftime("%d/%m/%Y %H:%M:%S")
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['apple'] = request.form["apple"]
    session['raspberry'] = request.form['raspberry']
    session['strawberry'] = request.form['strawberry']
    return redirect('/show')

@app.route('/show')
def show_checkout():
    return render_template("checkout.html",first_name = session['first_name'], last_name =  session['last_name'], student_id = session['student_id'], apple = int(session['apple']), raspberry = int(session['raspberry']), strawberry = int(session['strawberry']), time = session['time'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    