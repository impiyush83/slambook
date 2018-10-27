from flask_cors import CORS
from flask_restful import Api
from extensions import app
from urls import urls


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
        import pdb
        pdb.set_trace()


if __name__ == '__main__':
    app.run(debug=True)
