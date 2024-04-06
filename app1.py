## Building url dynamically
## flask variable rules and url binding

from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to the data science world'


@app.route('/success/<int:score>')
def success(score):
    return 'the person has passed and the marks is ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'the person has failed and the marks is ' + str(score)


##result checker
@app.route('/result/<int:score>')
def result(score):
    result=""
    if score<50:
        result="fail"
    else:
        result="pass"
    return result


if __name__=='__main__':
    app.run(debug=True)