import os

from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server
from slambook_restful.app import create_app
from slambook_restful.models import db
from slambook_restful.settings import ProdConfig, StageConfig, DevConfig, TestConfig

env = os.environ.get("SLAMBOOK_ENV").lower()
if env == 'prod':
    app = create_app(ProdConfig)
elif env == 'stage':
    app = create_app(StageConfig)
elif env == 'dev':
    app = create_app(DevConfig)
else:
    app = create_app(TestConfig)

migrate = Migrate(app=app, db=db)
manager = Manager(app=app)
manager.add_command('server', Server(threaded=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
