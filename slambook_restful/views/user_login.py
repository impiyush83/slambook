from flask import jsonify, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies


from slambook_restful.models.User.user import User
from slambook_restful.utils.custom_exceptions import NoResultFound, AuthenticationException
from slambook_restful.utils.utils import check_encrypted_password


def user_login(data):
    # get parser data
    # get user from database
    user = User.with_email_address(data.get("email"))
    unauth_msg = 'Email or password is wrong.'
    wrong_password = 'Password is wrong.'
    if user is None:
        raise NoResultFound("User not found")
    # check user password
    check = check_encrypted_password(data['password'], user.password)

    if not check_encrypted_password(data['password'], user.password):
        raise AuthenticationException(wrong_password)
    # if correct user password

    # create access token
    access_token = create_access_token(identity=user.id)

    # refresh_token = create_refresh_token(user.id)
    return access_token, user

