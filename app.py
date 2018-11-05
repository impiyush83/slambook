import os
from flask import Flask

from config import db_url
from models.db import get_session
from settings import DevConfig, TestConfig


def create_app(Config):
    # flask app configuration
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    # database session
    database_url = db_url
    if not database_url:
        raise ValueError("DATABASE-URL-NOT-SET")
    session = get_session(database_url=database_url)

    # teardown database session
    def close_session(response_or_exc):
        session.remove()
        return response_or_exc

    app.teardown_appcontext(close_session)
    return app


# main_app = create_app()
if __name__ == "__main__":
    env = os.environ.get("SLAMBOOK_ENV").lower()
    if env == 'dev':
        app = create_app(DevConfig)
    else:
        app = create_app(TestConfig)

    HERE = os.path.abspath(os.path.dirname(__file__))
    TEST_PATH = os.path.join(HERE, 'tests')
    from resource.flask_restful_api import restful_api
    restful_api(app)
    app.run(debug=True)
