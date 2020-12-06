from flask import Flask, render_template, request, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jalkjlksjmlqvkbmqoza'
db = SQLAlchemy(app)


class Company(db.Model):
    company_name = db.Column(db.String(200), primary_key=True)
    brand_name = db.Column(db.String(200), nullable=False)
    specialization = db.Column(db.String(256), nullable=False)
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
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    particular_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(100), default="")
    has_work = db.Column(db.Boolean, default=False)
    work_in = db.Column(db.String(256), default="")
    companies = db.Column(db.Text, default="")
    phone_number = db.Column(db.String(14), default="")
    password = db.Column(db.String(256), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())


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
            response = make_response(render_template("sign-up.html"))
            response.set_cookie('MarketPlace_username', user.email)
            return redirect('/')
        except:
            return "error"
    else:
        return render_template('sign-up.html')


@app.route('/sign-in/', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.get(username)
        if user is None:
            return render_template('sign-in.html',  data="<span class='text-danger'>Такой пользователь не существует</span>")
        elif user.password != password:
            return render_template('sign-in.html', data="<span class='text-danger'>Неверный пароль</span>")
        else:
            response = make_response(render_template("user.html"))
            response.set_cookie("MarketPlace_username", username)
            return redirect("/home/")
    else:
        return render_template('sign-in.html')


@app.route('/home/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        pass
    else:
        email = request.cookies.get("MarketPlace_username")
        if email is None:
            return redirect("/sign-in/")
        else:
            user = User.query.get(email)
            return render_template("user.html", data=user)


@app.route('/companies/', methods=['POST', 'GET'])
def companies():
    if request.method == "POST":
        pass
    else:
        companies = Company.query.order_by(Company.date.desc()).all()
        return render_template('companies.html', data = companies)


@app.route('/companies/<string:company_name>')
def view_company(company_name):
    company = Company.query.get(company_name)
    if company is None:
        return "Error 404"
    else:
        return render_template("company.html", data=company)

# Company admin panel
@app.route('/admin/', methods=['POST', 'GET'])
def admin(company_name):
    if request.method == "POST":
        pass
    else:
        return render_template("admin.html")

@app.route('/admin/support/', methods=['POST', 'GET'])
def admin_support():
    if request.method == 'POST':
        pass
    else:
        return render_template("admin_support.html")


@app.route('/companies/<string:company_name>/support/', methods=['POST', 'GET'])
def support(company_name):
    if request.method == 'POST':
        pass
    else:
        company = Company.query.get(company_name)
        if company is None:
            return "Error 404"
        return render_template("support.html", data=company)