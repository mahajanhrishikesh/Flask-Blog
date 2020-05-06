from flask import render_template, url_for, redirect, flash
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
	{
		'author':'Jan Vincent',
		'title':'Blog Post',
		'content':'First post content',
		'date_posted': 'April 20 2019'
	},
	{
		'author':'Jack Churchill',
		'title':'Blog Post Two',
		'content':'Second post content',
		'date_posted': 'April 25 2019'
	}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts, title='Home')

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com':
			if form.password.data == 'password':
				flash(f'You have been logged in!', 'success')
				return redirect(url_for('home'))
		else:
			flash(f'Incorrect username password!', 'danger')
	return render_template('login.html', title='Login', form=form)