from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key ="bimat"
@app.route('/')         
def index():
    if 'counter' in session:
        session['count'] += 1
        return render_template('index.html', counter = session['count'])
    else:
        session['count'] = 1
        return render_template('index.html', counter = session['count'])

@app.route('/count')
def count_num():
    session['count'] += 1
    return render_template("index.html", counter = session['count'])

@app.route('/reset')
def reset_num():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    