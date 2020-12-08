
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}'.format(
    username='andrhans',
    password='VSVw6ni1mzFAOc5M90GY',
    hostname='andrhans.mysql.pythonanywhere-services.com',
    databasename='andrhans$car-app',
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

app.secret_key = 'c8skRkkMostrhqioIWlC785ZnJEcvuFS'

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')