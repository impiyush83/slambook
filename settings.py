# -*- coding: utf-8 -*-
import os
os_env = os.environ


class Config(object):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_POOL_SIZE = 5


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = os_env.get('DEBUG', False)
    SQLALCHEMY_DATABASE_URI = os_env.get('SQLALCHEMY_DATABASE_URI',
                                         'postgresql://slambook:slambook@localhost:9011/slambook_dev')


class TestConfig(Config):
    ENV = 'test'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os_env.get('TEST_DB_URI',
                                         'postgresql://slambook:slambook@localhost:9011/slambook_test')
    SQLALCHEMY_SESSION_OPTIONS = dict(echo=False)
