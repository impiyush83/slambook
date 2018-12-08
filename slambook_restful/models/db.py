import os

from flask import Config
from sqlalchemy_wrapper import SQLAlchemy

config_name = 'slambook_restful.settings.{}Config'.format(os.environ.get('SLAMBOOK_ENV'))
config = Config("")
config.from_object(config_name)

db = SQLAlchemy(uri=config['DATABASE_URL'])