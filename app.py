import os
from flask import Flask
from sqlalchemy_wrapper import SQLAlchemy

from resource.flask_restful_api import restful_api

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(uri=app.config['SQLALCHEMY_DATABASE_URI'])

# add models you want to migrate
from models.friend import Friend
from models.user import User
from models.secret import Secret
from database import Base
from database import SurrogatePK
from database import HasTablename

if __name__ == '__main__':
    restful_api(app)
    app.run(debug=True)
