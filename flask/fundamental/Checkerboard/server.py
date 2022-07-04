from turtle import width
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",color1 = "red",color2 = "black", width = int(8/2), height = int(8/2))

@app.route('/<int:x>')
def chest_x(x):
    return render_template("index.html",color1 = "red",color2 = "black", width = int(x/2), height = int(4/2))


@app.route('/<int:x>/<int:y>')
def chest_xy(x,y):
    return render_template("index.html",color1 = "blue",color2 = "black", width = int(x/2), height = int(y/2))

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def chest_color(x,y,color1,color2):
    return render_template("index.html",color1 = color1,color2 = color2, width = int(x/2), height = int(y/2))
if __name__ == "__main__":
    app.run(debug=True)
