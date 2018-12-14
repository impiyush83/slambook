from flask import current_app as app, request, make_response, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from constants.common_constants import headers
from slambook_restful.schemas.register_customer import transfer_profile_data
from slambook_restful.utils.resource_exceptions import exception_handle
from slambook_restful.utils.validators import ajax_request_data_validator_restful
from slambook_restful.views.transfer_profile_to_secret_key_bearer import transfer_profile


class CustomerDataTransfer(Resource):
    decorators = [jwt_required, exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    @ajax_request_data_validator_restful(transfer_profile_data)
    def post(self):
        """

    .. http:post::  /user/transfer

        This api will be used to transfer profile to another

        **Example request**:

        .. sourcecode:: http

           POST  /user/transfer HTTP/1.1
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
           }

        :statuscode 200: json
        :statuscode 400: value error

        """
        data = request.json
        transfer_profile(data)
        return make_response(jsonify(headers))
