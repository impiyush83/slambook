import os

from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from slambook_restful.models.User.user import User
from slambook_restful.models.Friend.friend import  Friend
from slambook_restful.models.Secret.secret import Secret
from slambook_restful.flask_restful_api import restful_api
from slambook_restful.models.db import db


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    restful_api(app)
    migrate = Migrate(app=app, db=db)
    migrate.init_app(app)
    app.config['JWT_SECRET_KEY'] = os.urandom(24)
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    jwt = JWTManager(app)
    return app
