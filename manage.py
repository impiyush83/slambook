from flask_script import Manager, Server
from flask_migrate import MigrateCommand, Migrate

from slambook_restful.app.app import create_app


app = create_app()
manager = Manager(app)
migrate = Migrate(compare_type=True)
manager.add_command('server', Server(threaded=True))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

