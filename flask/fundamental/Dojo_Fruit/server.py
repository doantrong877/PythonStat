from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def creater_user():
    print("Got Post Info")
    print(request.form['name'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)