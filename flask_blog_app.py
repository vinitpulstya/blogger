from flask import Flask, render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '00e6e9abfb7f323f265efcfd93947a48'

post = [
	{
		'author'	:	'Pulstya',
		'title'	:	'Blog Post1',
		'content'	:	'first content',
		'date_posted'	:	'October 28 2020'
	},
	{
		'author'	:	'Vinit',
		'title'	:	'Blog Post2',
		'content'	:	'second content',
		'date_posted'	:	'October 30 2020'
	}
]


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts = post)

@app.route('/about')
def about():
	return render_template('about.html', title = 'About')
	
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('Logged In!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccesful', 'danger')
	return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
	app.run(debug= True)
