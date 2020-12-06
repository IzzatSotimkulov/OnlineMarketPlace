from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jalkjlksjmlqvkbmqoza'
db = SQLAlchemy(app)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(200), nullable=False)
    brand_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    date = db.Column(db.DateTime, nullable=False)
    index = db.Column(db.String(100), nullable=False)
    inn = db.Column(db.String(9), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(30), default='')
    email = db.Column(db.String(30), nullable=False)
    site = db.Column(db.String(100), default="")
    phone_numbers = db.Column(db.String(256), default="")
    posts_ids = db.Column(db.Text, default="")
    vacancies_ids = db.Column(db.Text, default="")
    products_ids = db.Column(db.Text, default="")
    workers_ids = db.Column(db.Text, default="")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    particular_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), default="")
    has_work = db.Column(db.Boolean, default=False)
    work_in = db.Column(db.String(256), default="")
    companies = db.Column(db.Text, default="")
    phone_number = db.Column(db.String(14), default="")
    password = db.Column(db.String(256), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign-up/', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        user = User(name = request.form['first_name'], email = request.form['email'], surname = request.form['last_name'], particular_name = request.form['particular_name'], password = request.form['password'])
        try:
            db.session.add(user)
            db.session.commit()
        except:
            return "Error while reqistration!"
    else:
        return render_template('sign-up.html')


@app.route('/sign-in/', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

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


@app.route('/companies/<string:company_name>', methods=['POST','GET'])
def view_company(company_name):
    pass


@app.route('/admin/', methods=['POST', 'GET'])
def add_product(company_name):
    if request.method == "POST":
        pass
    else:
        return render_template("add_product.html")


app.run(debug=True)
