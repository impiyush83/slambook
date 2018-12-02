import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = "postgresql://slambook:slambook@localhost/slambook_prod"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "postgresql://slambook:slambook@localhost/slambook_stage"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "postgresql://slambook:slambook@localhost/slambook_dev"


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = "postgresql://slambook:slambook@localhost/slambook_test"
