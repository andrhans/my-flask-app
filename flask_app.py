
from flask import Flask, render_template, request, redirect, session
from flask_login import login_required, current_user, login_user, logout_user
from models import login, db, UserModel

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

@app.route('/blog')
@login_required
def blog():
    if current_user.is_authenticated:
        return render_template('blog.html')
    else:
        session['logged_in'] = False
        return redirect('/')

@app.route('/', methods=['POST', 'GET'])
def login():
    """Login header signs in automatically. Fix it"""
    if current_user.is_authenticated:
        return redirect('/blog')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username != 'admin' or password != 'adminpass':
            error = 'Invalid Credentials. Please try again.'
            return error
        else:
            session['logged_in'] = True
            return redirect('/')

#
#   CAN'T MAKE THIS WORK!
#        user = UserModel.query.filter_by(username = username).first()
#        if user is not None and user.check_password(request.form['password']):
#            login_user(user)
#            return redirect('/blog')

    return render_template('blog.html')

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
            return("Email already in our database!")

        user = UserModel(username=username, password=password, cvr=cvr, email=email)
        db.session.add(user)
        db.session.commit()
        return 'Successfully inserted data!'
    return render_template('register.html')

@app.route('/logout')
def logout():
    """Logout users"""
    logout_user()
    return redirect('/')

