import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from resource.flask_restful_api import restful_api

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


if __name__ == "__main__":
    restful_api(app)
    app.run(debug=True)
