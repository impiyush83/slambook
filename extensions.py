import os
from flask import Flask
from sqlalchemy_wrapper import SQLAlchemy


# created db object
db = SQLAlchemy('sqlite:///slambook.db')
# creates flask app object
app = Flask(__name__)
app.secret_key = os.urandom(24)


