from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('users/login.html')

@views.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('users/login.html')

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('users/signup.html')

@views.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    return render_template('users/edit_profile.html')

@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@views.route('/classes')
def classes():
    return render_template('classes.html')

@views.route('/assignments')
def assignments():
    return render_template('assignments.html')
