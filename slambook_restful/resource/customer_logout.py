from flask import current_app as app, jsonify, url_for
from flask_jwt_extended import jwt_required, unset_jwt_cookies
from flask_restful import Resource
from werkzeug.utils import redirect

from slambook_restful.resource.customer_signup import CustomerSignUp
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

           POST  /user/login HTTP/1.1
           {
             "email" : "nalawadepiyush@gmail.com",
             "password" : "Piyush"
           }

        **Example response**:


        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept
           Content-Type: application/json
           {
                "access_token" : "sfwfwf",
                "refresh_token": "wfgwfwgw"
           }

        :statuscode 200: json
        :statuscode 400: value error

        """
        resp = jsonify({'logout': True})
        unset_jwt_cookies(resp)
        return resp