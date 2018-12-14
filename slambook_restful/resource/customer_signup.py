from flask import current_app as app, request, make_response, render_template
from flask_restful import Resource

from constants.common_constants import headers
from slambook_restful.schemas.register_customer import register_user
from slambook_restful.utils.resource_exceptions import exception_handle
from slambook_restful.utils.validators import ajax_request_data_validator_restful
from slambook_restful.views.user_registration import user_registration


class CustomerSignUp(Resource):
    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    @ajax_request_data_validator_restful(register_user)
    def post(self):
        """

    .. http:post::  /user/signup

        This api will be used to signup user

        **Example request**:

        .. sourcecode:: http

           POST  /user HTTP/1.1
           {
             "first_name" : Piyush,
             "last_name" : Nalawade,
             "password" : pict123 ,
             "gender" : Male,
             "favourite_color" : Red,
             "favourite_food" : Chinese,
             "favourite_song" : XYZ ,
             "mobile" : 7875451222
           }

        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept
           Content-Type: application/json
           {
           }

        :statuscode 200: empty json
        :statuscode 400: value error

        """

        data = request.json
        user_registration(data)
        return make_response(render_template('login_and_sign_up.html'), 200, headers)

