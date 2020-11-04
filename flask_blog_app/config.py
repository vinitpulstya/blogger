import os

class Config:
    SECRET_KEY = '00e6e9abfb7f323f265efcfd93947a48'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('USER_MAIL')
    MAIL_PASSWORD = os.environ.get('USER_PASS')
    MAIL_USE_TLS = False