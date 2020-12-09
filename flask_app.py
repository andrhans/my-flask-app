
from flask import Flask, render_template, request, redirect, session, url_for
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

@app.route('/', methods=['GET', 'POST'])
def login():
    """Login header signs in automatically. Fix it"""
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username != 'admin' or password != 'adminpass':
            error = 'Invalid Credentials. Please try again.'
            return render_template('index.html', error=error)
        else:
            session['logged_in'] = True
            return redirect(url_for('profile'))

#
#   CAN'T MAKE THIS WORK!
#        user = UserModel.query.filter_by(username=username, password=password).all()
#        if user is not None:
#            login_user(user)
#            return redirect('/profile')
    return render_template('index.html')

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
            error = 'username already in our database!'
            return render_template('register.html', error=error)

        user = UserModel(username=username, password=password, cvr=cvr, email=email)
        db.session.add(user)
        db.session.commit()
        return 'Successfully inserted data!'
    return render_template('register.html')

@app.route('/logout')
def logout():
    """Logout for users"""
    logout_user()
    return 'You have successfully logged out!'
    session['logged_in'] = False

#@app.route('/blog')
#@login_required
#def blog():
#    """Check this out... weird problem"""
#    if current_user.is_authenticated:
#        return render_template('blog.html')
#    else:
#        session['logged_in'] = False
#        return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


