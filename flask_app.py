
from flask import Flask, render_template, request, redirect, session, url_for, flash
from functools import wraps
from models import login, db, UserModel, CarModel

app = Flask(__name__)

login.init_app(app)
#login.login_view = 'login'
#login.logout_view = 'logout'

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
db.init_app(app)

app.secret_key = 'c8skRkkMostrhqioIWlC785ZnJEcvuFS'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    """Display routing possibilities"""
    return render_template('index.html')

@app.route('/find')
def find():
    """Find plate number"""
    return render_template('searchcar.html')

@app.route('/dummycar')
def dummycar():
    return render_template('dummycar.html')

# Find out what happens in this one
#@app.route('/car/<registration_id>')
#def car(registration_id):
#    cars = CarModel.query.filter_by(registration_id=registration_id).first()
#    return render_template('createcar.html', cars=cars)

@app.route('/cars')
def list():
   cars = CarModel.query.all()
   return render_template('carlist.html', cars=cars)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login for registered user admin... finish research..."""
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserModel.query.filter_by(username=username, password=password).one()
        if user is None:
           error= ' Incorrect username or password. Please try again.'

        else:
            session['logged_in'] = True
            flash('You are now logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['POST', 'GET'])
def register():
    """Register new users successfully"""
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cvr = request.form['cvr']
        email = request.form['email']

        if UserModel.query.filter_by(username=username).first():
            error = 'Username already in our database!'
            return render_template('register.html', error=error)

        user = UserModel(username=username, password=password, cvr=cvr, email=email)
        db.session.add(user)
        db.session.commit()
        return 'Successfully inserted data!'
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    """Logout for users"""
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))



