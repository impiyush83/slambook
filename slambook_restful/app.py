from flask import Flask

from slambook_restful.flask_restful_api import restful_api
from slambook_restful.models import db


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    restful_api(app)
    return app