
from flask import Flask, render_template, request, redirect, session, url_for, flash
from functools import wraps
from models import login, db, UserModel, CarModel
import urllib.request
import json

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
    return render_template('searchcar.html')

@app.route('/find-car', methods=['GET', 'POST'])
def fcar():
    """Find plate number. First if checks for input and loads the url of the api.
    The second if checks that the loaded json object (license plate) belongs to a car.
    Then, pass the data through the template and finally, send the data to the db"""
    if request.method=='POST':
        license=request.form['plate']
        api_token='pnW5hV7uOqj0PoScLJe1qKVoavT6fJc1Jvw0iGdvaYNzv4riuaGE8HvJx1EYoit8'
        url="http://api.nrpla.de/"+license+"?api_token="+api_token
        data=urllib.request.urlopen(url).read().decode()

        obj=json.loads(data)

        type=(obj['data']['type'])

        if type == "Personbil":
            registration_id=obj['data']['registration']
            brand=(obj['data']['brand'])
            model=(obj['data']['model'])
            version=(obj['data']['version'])
            fuel_type=(obj['data']['fuel_type'])
            model_year=(int['data']['model_year'])
            engine_power=(int['data']['engine_power'])
            fuel_efficiency=(int['data']['fuel_efficiency'])
            engine_cylinders=(int['data']['engine_cylinders'])
            top_speed=(int['data']['top_speed'])
            doors=(int['data']['doors'])
            minimum_seats=(int['data']['minimum_seats'])
            axles=(int['data']['axles'])
            drive_axles=(int['data']['drive_axles'])

            car=CarModel(registration_id=registration_id,brand=brand,model=model,
            version=version,fuel_type=fuel_type,model_year=model_year,
            engine_power=engine_power,fuel_efficiency=fuel_efficiency,
            engine_cylinders=engine_cylinders,top_speed=top_speed,doors=doors,
            minimum_seats=minimum_seats, axles=axles, drive_axles=drive_axles)
            db.session.add(car)
            db.session.commit()

            flash('Car data saved')

            fcar=CarModel.query.filter_by(registration_id=registration_id).one()
            return render_template('fcar.html', cars=fcar)
        else:
            error='The plate does not belong to a car'
            return render_template('searchcar.html', error=error)
    else:
        error='Did you insert a number plate?'
    return render_template('searchcar.html', error=error)

@app.route('/dummycar')
def dummycar():
    return render_template('dummycar.html')

@app.route('/cars')
def list():
   cars=CarModel.query.all()
   return render_template('carlist.html', cars=cars)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login for all users implemented with query!"""
    error=None
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        user=UserModel.query.filter_by(username=username, password=password).one()
        if user is None:
           error=' Incorrect username or password. Please try again.'
        else:
            session['logged_in'] = True
            flash('You are now logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['POST', 'GET'])
def register():
    """Register new users successfully"""
    if request.method=='GET':
        return render_template('register.html')

    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cvr=request.form['cvr']
        email=request.form['email']

        if UserModel.query.filter_by(username=username).first():
            error='Username already in our database!'
            return render_template('register.html', error=error)

        user=UserModel(username=username, password=password, cvr=cvr, email=email)
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



