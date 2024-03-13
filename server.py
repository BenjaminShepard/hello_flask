from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/success')  # 
def success():
    return "success"

# @app.route('/hello/<name>') # for a route '/hello/___' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     return f"Hello {name}"

# We  can add as many of these as we need, giving each variable a different name:
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    return f"Username: {username}, id: {id}"

# Here the second parameter is cast into an integer before being passed to the function
@app.route('/hello/<name>/<int:num>') 
def hello(name, num):
    return f"Hello, {name * num}"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode
    
