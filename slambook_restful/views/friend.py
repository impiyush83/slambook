from slambook_restful.models.Friend.friend import Friend
from slambook_restful.utils.custom_exceptions import ResourceAlreadyPresent


def save_new_friend(user, data):
    if user.email == data.get('email'):
        raise ResourceAlreadyPresent("Its your email id !! You cant be your friend !!")
    is_duplicate = Friend.check_if_duplicate_friend(user, data)
    is_current_user = Friend.check_if_current_user(user, data)
    if is_duplicate:
        raise ResourceAlreadyPresent("Your already have friend with this email address")
    if is_current_user:
        raise ResourceAlreadyPresent("Its your email id !! Dont Create your entry as your friend")
    Friend.add_friend_details(user, data)


def add_new_friend_remote(bearer, data):
    is_duplicate = Friend.check_if_duplicate_friend(bearer, data)
    if is_duplicate:
        raise ResourceAlreadyPresent("Your entry is already present at your friend !! ")
    Friend.add_friend_details(bearer, data)

