import os

from flask import Flask
from flask_script import Manager, Server
from flask_migrate import MigrateCommand, Migrate
from sqlalchemy_wrapper import SQLAlchemy

from slambook_restful.flask_restful_api import restful_api
from slambook_restful.settings.config import ProdConfig, StageConfig, DevConfig, TestConfig


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    restful_api(app)
    return app


env = os.environ.get("SLAMBOOK_ENV").lower()
if env == 'prod':
    app = create_app(ProdConfig)
elif env == 'stage':
    app = create_app(StageConfig)
elif env == 'dev':
    app = create_app(DevConfig)
else:
    app = create_app(TestConfig)
db = SQLAlchemy(uri=app.config['SQLALCHEMY_DATABASE_URI'], app=app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('server', Server(threaded=True))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

