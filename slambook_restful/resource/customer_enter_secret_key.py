from flask import current_app as app, render_template, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from constants.common_constants import headers
from slambook_restful.models.User.user import User
from slambook_restful.utils.resource_exceptions import exception_handle


class CustomerEnterSecretKey(Resource):

    decorators = [jwt_required, exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def get(self):
        """

    .. http:get::  /user/enter-secret-key

        This api will be used to create secrete key

        **Example request**:

        .. sourcecode:: http


        **Example response**:


        .. sourcecode:: http


           HTTP/1.1 200 OK
           Vary: Accept
           Content-Type: application/json
           {

           }

        :statuscode 200: json
        :statuscode 400: value error

        """
        user_id = get_jwt_identity()
        user = User.with_id(user_id)
        return make_response(
            render_template('enter_secret_key.html'),
            headers)
