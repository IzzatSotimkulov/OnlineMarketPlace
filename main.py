from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    okonh_code = db.Column(db.Integer, nullable=False)
    date = datetime.now()


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
def home():
    if request.method == "POST":
        pass
    else:
        return render_template('user.html')


@app.route('/companies/', methods=['POST', 'GET'])
def companies():
    if request.method == "POST":
        pass
    else:
        companies = Company.query.order_by().all()
        return render_template('companies.html', data = companies)




app.run(debug=True)
