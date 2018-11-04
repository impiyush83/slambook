
from extensions import app
from flask_restful_api import restful_api

if __name__ == '__main__':
    restful_api(app)
    app.run(debug=True)