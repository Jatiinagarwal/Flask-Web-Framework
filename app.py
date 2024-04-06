from flask import Flask
### WSGI application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the world of data science"

@app.route('/members')
def members():
    return "Welcome to the world of data science members please"


if __name__=='__main__':
    app.run(debug=True)