from flask import current_app as app, request, make_response, render_template
from flask_jwt_extended import set_access_cookies
from flask_restful import Resource

from constants.common_constants import headers
from slambook_restful.models.Friend.friend import Friend
from slambook_restful.models.Secret.secret import Secret
from slambook_restful.schemas.register_customer import login_user
from slambook_restful.utils.resource_exceptions import exception_handle
from slambook_restful.utils.validators import ajax_request_data_validator_restful
from slambook_restful.views.user_login import user_login


class CustomerLogin(Resource):
    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    @ajax_request_data_validator_restful(login_user)
    def post(self):
        """

    .. http:post::  /user/login

        This api will be used to signup user

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
        data = request.json
        access_token, user = user_login(data)
        # headers['access_token'] = tokens['access_token']
        friends = Friend.get_friends_with_email_address(user.id)
        is_secret_key_created = Secret.is_secret_key_created(user.email)

        response = make_response(
            render_template('homepage.html',
                            friends=friends,
                            len=len(friends),
                            is_secret_key=is_secret_key_created),
            headers
        )
        # create access token cookie
        set_access_cookies(response, access_token)

        return response