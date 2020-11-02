import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = '00e6e9abfb7f323f265efcfd93947a48'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('USER_MAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('USER_PASS')
app.config['MAIL_USE_TLS'] = False

mail = Mail(app)

from flask_blog_app import routes