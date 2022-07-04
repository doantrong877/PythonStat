from flask import Flask,render_template
app = Flask(__name__)

@app.route('/play')
def home():
    return render_template("index.html",times = 3,color = "blue")

@app.route('/play/<int:times>')
def play_2(times):
    return render_template("index.html",times=times,color="blue")

@app.route("/play/<int:times>/<string:color>")
def play_3(times,color):
    return render_template("index.html", times=times, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.