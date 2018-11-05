from wsgiref import headers

from flask import render_template, make_response, app
from flask_restful import Resource
from constants.common_constants import headers
from utils.resource_exceptions import exception_handle


class Index(Resource):
    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def get(self):
        """

    .. http:get::  /

        This api will be used to showcase homepage

        **Example request**:

        .. sourcecode:: http

           GET  /user  HTTP/1.1

        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: value error

        """
        return make_response(render_template('login_and_sign_up.html'), 200, headers)
