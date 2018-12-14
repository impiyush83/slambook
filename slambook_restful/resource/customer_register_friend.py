from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import current_app as app, render_template, make_response

from constants.common_constants import headers
from slambook_restful.models.User.user import User
from slambook_restful.utils.resource_exceptions import exception_handle


class OnSpotRegisterFriend(Resource):
    decorators = [jwt_required, exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def get(self):
        """

    .. http:get::  /user/register-friend

        This api will be used to showcase homepage

        **Example request**:

        .. sourcecode:: http

           GET  /user/register-friend  HTTP/1.1

        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """

        user_id = get_jwt_identity()
        user = User.with_id(user_id)
        return make_response(render_template('registration.html', page_render=True), headers)
