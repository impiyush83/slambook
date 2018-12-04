from slambook_restful.models.User.user import User
from slambook_restful.utils.custom_exceptions import ResourceAlreadyPresent


def user_registration(data):
    try:
        User.insert_user(data)
    except:
        raise ResourceAlreadyPresent("User already exists with this email address")