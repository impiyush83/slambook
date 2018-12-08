from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from slambook_restful.app import create_app
from slambook_restful.settings import DevConfig

# env = os.environ.get("SLAMBOOK_ENV").lower()
# if env == 'prod':
#     app = create_app(ProdConfig)
# elif env == 'stage':
#     app = create_app(StageConfig)
# elif env == 'dev':
#     app = create_app(DevConfig)
# else:
#     app = create_app(TestConfig)
app = create_app(DevConfig)
# migrate = Migrate(app=app, db=db, compare_type=True)
manager = Manager(app=app)
manager.add_command('server', Server(threaded=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
