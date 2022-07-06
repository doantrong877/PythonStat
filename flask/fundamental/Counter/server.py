from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key ="bimat"
@app.route('/')         
def index():
    if 'count' in session:
        if "add" in session:
            session['count'] += 2
            session.pop('add')
        else:
            session['count'] += 1
        return render_template('index.html', counter = session['count'])
    else:
        session['count'] = 1
        return render_template('index.html', counter = session['count'])

@app.route('/count')
def count_num():
    session['count'] += 1
    return render_template("index.html", counter = session['count'])

@app.route('/destroy_session')
def reset_num():
    session.clear()
    return redirect('/')

@app.route('/add')
def add_num():
    session["add"] = True
    return redirect('/')

@app.route('/increment', methods = ['POST'])
def increment_num():
    session["count"] =session["count"] + int(request.form['inp']) - 1
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    