from flask_cors import CORS
from flask_restful import Api

import urls
from extensions import app


def restful_api(app):
    CORS(app, resources={r"/*": {"origins": "*"}})

    api = Api(app, prefix='/')
    for url in urls:
        api.add_resource(
            url.resource,
            url.name,
            *url.endpoint,
            strict_slashes=False
        )

if __name__ == '__main__':
    app.run(debug=True)
