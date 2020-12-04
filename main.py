from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign-up/', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        pass
    else:
        return render_template('sign-up.html')


@app.route('/sign-in/', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        pass
    else:
        return render_template('sign-in.html')


@app.route('/home/', methods=['POST', 'GET'])
def sign_up():
    if request.method == "POST":
        pass
    else:
        return render_template('user.html')


app.run(debug=True)
