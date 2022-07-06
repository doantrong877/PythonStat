from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "bimat"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getInfo', methods=['POST'])
def info():
    session['city'] = request.form['city']
    session['username'] = request.form['username']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def result():
    return render_template('info.html',name = session['username'],city = session['city'], language=session['language'], comment= session['comment'])


if __name__ == "__main__":
    app.run(debug=True)