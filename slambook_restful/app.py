import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

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
    app.config['JWT_ACCESS_COOKIE_NAME'] = ''
    jwt = JWTManager(app)
    return app
