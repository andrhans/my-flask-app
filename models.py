
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login = LoginManager()
db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))
    cvr = db.Column(db.String(80))
    email = db.Column(db.String(128))

    def __init__(self, username, password, cvr, email):
        self.username = username
        self.password = password
        self.cvr = cvr
        self.email = email

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return UserModel.query.get(int(id))

class CarModel(db.Model):
    __tablename__= "cars"

    id = db.Column(db.Integer, primary_key=True)
    registration_id = db.Column(db.String(128),unique=True)
    brand = db.Column(db.String(80))
    model = db.Column(db.String(80))
    version = db.Column(db.String(128))
    fuel_type = db.Column(db.String(80))
    model_year = db.Column(db.Integer)
    engine_power = db.Column(db.Integer)
    fuel_efficiency = db.Column(db.String(80))
    engine_cylinders = db.Column(db.Integer)
    top_speed = db.Column(db.Integer)
    doors = db.Column(db.Integer)
    minimum_seats = db.Column(db.Integer)
    axles = db.Column(db.Integer)
    drive_axles = db.Column(db.Integer)

    def __init__(self,registration_id,brand,model,version,fuel_type,model_year,engine_power,fuel_efficiency,engine_cylinders,top_speed,doors,minimum_seats,axles,drive_axles):
        self.registration_id = registration_id
        self.brand = brand
        self.model = model
        self.version = version
        self.fuel_type = fuel_type
        self.model_year = model_year
        self.engine_power = engine_power
        self.fuel_efficiency = fuel_efficiency
        self.engine_cylinders = engine_cylinders
        self.top_speed = top_speed
        self.doors = doors
        self.minimum_seats = minimum_seats
        self.axles = axles
        self.drive_axles = drive_axles


