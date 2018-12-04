from flask import Flask

from slambook_restful.flask_restful_api import restful_api


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    restful_api(app)
    return app
