from flask import current_app as app, jsonify
from flask_jwt_extended import unset_jwt_cookies
from flask_restful import Resource

from slambook_restful.utils.resource_exceptions import exception_handle


class CustomerLogout(Resource):
    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def post(self):
        """

    .. http:post::  /user/logout

        This api will be used to logout user

        **Example request**:

        .. sourcecode:: http

           POST  /user/logout HTTP/1.1
           { }

        **Example response**:


        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept
           Content-Type: application/json
           { }

        :statuscode 200: json
        :statuscode 400: value error

        """
        resp = jsonify({'logout': True})
        unset_jwt_cookies(resp)
        return resp
