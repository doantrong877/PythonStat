from flask import Flask,render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name.capitalize()}"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num,name):
    return num*name


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    print("Wrong URL")
    app.run(debug=True)    # Run the app in debug mode.

