from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mailman import Mail
from flask_wtf.csrf import CSRFProtect
import os
from flask_cors import CORS


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'negmatovazam4@gmail.com'
app.config['MAIL_PASSWORD'] = '123qweasdghost'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hard to guess'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False
csrf = CSRFProtect(app)
cors = CORS(app, resources={r"/export/*": {"origins": "*"}})
mailman = Mail(app=app)
db = SQLAlchemy(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'sign_in'

from application import routes, model