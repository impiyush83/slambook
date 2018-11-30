from flask import current_app as app
from flask_restful import Resource

# from utils.resource_exceptions import exception_handle


class User(Resource):
    # decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    # def get(self):
    #     """
    #
    # .. http:get::  /user/<:int>
    #
    #     This api will be used to login user
    #
    #     **Example request**:
    #
    #     .. sourcecode:: http
    #
    #        GET  /user  HTTP/1.1
    #
    #     **Example response**:
    #
    #     .. sourcecode:: http
    #
    #        HTTP/1.1 200 OK
    #        Vary: Accept
    #        Content-Type: application/json
    #        {
    #                 "auth_token" : '<auth_token>'
    #        }
    #
    #     :statuscode 200: response with auth token
    #     :statuscode 400: value error
    #
    #     """
    #     import pdb
    #     pdb.set_trace()
    #     fn = request.form['fn']
    #     sn = request.form['sn']
    #     email = request.form['email']
    #     password = request.form['pass']
    #     gender = request.form['gender']
    #     u1 = Parent(fn=fn, sn=sn, email=email, password=password, gender=gender)
    #     db.add(u1)
    #     db.commit()
    #     return redirect(url_for('index'))
    #     return redirect(url_for('index'))

    # def post(self):
    #     """
    #
    # .. http:post::  /user
    #
    #     This api will be used to signup user
    #
    #     **Example request**:
    #
    #     .. sourcecode:: http
    #
    #        POST  /user HTTP/1.1
    #
    #     **Example response**:
    #
    #     .. sourcecode:: http
    #
    #        HTTP/1.1 200 OK
    #        Vary: Accept
    #        Content-Type: application/json
    #        {
    #        }
    #
    #     :statuscode 200: empty json
    #     :statuscode 400: value error
    #
    #     """
    #     import pdb
    #     pdb.set_trace()
    #     fn = request.form['fn']
    #     sn = request.form['sn']
    #     email = request.form['email']
    #     password = request.form['pass']
    #     gender = request.form['gender']
    #     u1 = Parent(fn=fn, sn=sn, email=email, password=password, gender=gender)
    #     db.add(u1)
    #     db.commit()
    #     return redirect(url_for('index'))
