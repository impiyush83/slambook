from flask import current_app as app, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from slambook_restful.models.User.user import User
from slambook_restful.utils.resource_exceptions import exception_handle
from slambook_restful.views.friend import save_new_friend


class SaveFriend(Resource):

    decorators = [jwt_required, exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def post(self):
        """

    .. http:post::  /user/save

        This api will be used to showcase homepage

        **Example request**:

        .. sourcecode:: http

           POST  /user/save  HTTP/1.1

        **Example response**:

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """
        data = request.json
        user_id = get_jwt_identity()
        user = User.with_id(user_id)
        save_new_friend(user, data)
