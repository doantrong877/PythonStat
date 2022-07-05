from flask import Flask, render_template,redirect, session

app = Flask(__name__)
app.secret_key ="bimat"
session['counter'] = 0

@app.route('/')
def get_info():
    session['counter'] += 1
    return render_template('index.html',count = session['counter'] )
    

@app('/click', methods =['POST'])
def click():
    session['counter'] += 1
    return redirect('/count')

@app('/count')
def count():
    return render_template('index.html',count = session['counter'])

@app('/reset', methods = ['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

if __name__ == '__main__':
    app.run(debug == True)