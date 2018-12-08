import os

from flask import Config
from sqlalchemy_wrapper import SQLAlchemy

from manage import app

config_name = 'slambook_restful.settings.{}Config'.format(os.environ.get('SLAMBOOK_ENV'))
config = Config("")
config.from_object(config_name)

db = SQLAlchemy(uri=app.config['DATABASE_URL'])