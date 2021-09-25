#Import flask module
from flask import Flask

#Declare app instance
app = Flask(__name__)

#Define Home Page with Hello World
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#Define user page with Hello Name
#Using dynamic route
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
