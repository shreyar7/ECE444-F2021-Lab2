#Import flask module
from flask import Flask

#Declare app instance
app = Flask(__name__)

#Define Home Page
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
