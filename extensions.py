import os

from flask_migrate import Migrate
from sqlalchemy_wrapper import SQLAlchemy
from flask.config import Config

from manage import app

config_name = 'slambook.config.{}Config'.format(os.environ.get('APP_SETTINGS'))
config = Config("")
config.from_object(config_name)

db = SQLAlchemy(uri=app.config['SQLALCHEMY_DATABASE_URI'])
migrate = Migrate(compare_type=True)
