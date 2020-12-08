
from flask import Flask, render_template, request, redirect
from flask_login import login_required, current_user, login_user, logout_user
from models import login, db, UserModel

app = Flask(__name__)

login.init_app(app)
login.login_view = 'login'

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

app.secret_key = 'c8skRkkMostrhqioIWlC785ZnJEcvuFS'

@app.route('/blog')
@login_required
def blog():
    if current_user.is_authenticated:
        return render_template('blog.html')

@app.route('/', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/blog')

    if request.method == 'POST':
        username = request.form['username']
        user = UserModel.query.filter_by(username = username).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/blog')

    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/blog')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cvr = request.form['cvr']

        if UserModel.query.filter_by(email=email).first():
            return("Email already in our database!")

        user = UserModel(email=email, username=username, cvr=cvr)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/blog')

