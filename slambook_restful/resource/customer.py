# from flask import current_app as app, request
# from flask_restful import Resource
#
#
# class Customer(Resource):
#
#     def __init__(self):
#         app.logger.info('In the constructor of {}'.format(self.__class__.__name__))
#
#     def post(self):
#         """
#
#     .. http:post::  /user
#
#         This api will be used to signup user
#
#         **Example request**:
#
#         .. sourcecode:: http
#
#            POST  /user HTTP/1.1
#
#         **Example response**:
#
#         .. sourcecode:: http
#
#            HTTP/1.1 200 OK
#            Vary: Accept
#            Content-Type: application/json
#            {
#            }
#
#         :statuscode 200: empty json
#         :statuscode 400: value error
#
#         """
#         import pdb
#         pdb.set_trace()
#         data = request.form
#         # User.insert_user(data)
#         # return make_response(render_template('login_and_sign_up.html'), 200, headers)
