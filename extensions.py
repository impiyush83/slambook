from sqlalchemy_wrapper import SQLAlchemy
from flask.config import Config
import os

config_name = 'smartcook.settings.{}Config'.format(os.environ.get('SMARTCOOK_ENV'))
config = Config("")
config.from_object(config_name)

db = SQLAlchemy(
    uri=config['SQLALCHEMY_DATABASE_URI'],
    pool_size=config['SQLALCHEMY_POOL_SIZE'],
    pool_recycle=300,
    pool_pre_ping=True,  # tests connections for liveness upon each checkout. By firing select 1; query
    pool_timeout=30,  # – number of seconds to wait before giving up on getting a connection from the pool.
    **config.get('SQLALCHEMY_SESSION_OPTIONS', {})
)

