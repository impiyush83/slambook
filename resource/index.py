from flask_restful import Resource

from extensions import app
from utils.resource_exceptions import exception_handle


class Index(Resource):
    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def get(self):
        """

    .. http:get::  /

        This api will be used to login user

        **Example request**:

        .. sourcecode:: http

           GET  /user  HTTP/1.1

        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept
           Content-Type: application/json
           {
                    "auth_token" : '<auth_token>'
           }

        :statuscode 200: response with auth token
        :statuscode 400: value error

        """
        pass