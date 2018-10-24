import os

from flask import Flask
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///slambook.db')
app = Flask(__name__)
app.secret_key = os.urandom(24)
