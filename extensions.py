import os

from flask import Flask
from flask_login import LoginManager
from sqlalchemy_wrapper import SQLAlchemy

from utils.flask_login_manager import SmartLoginManager

# created db object
db = SQLAlchemy('sqlite:///slambook.db')
# creates flask app object
app = Flask(__name__)
app.secret_key = os.urandom(24)


# flask login and login manager
login_manager = LoginManager()
login_manager.init_app(app)

# new login managers can be created
user_login_manager = SmartLoginManager('user')
