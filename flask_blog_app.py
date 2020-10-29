from flask import Flask, render_template,url_for
app = Flask(__name__)

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
    
if __name__ == '__main__':
	app.run(debug= True)
