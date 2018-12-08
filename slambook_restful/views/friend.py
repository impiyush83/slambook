from slambook_restful.models.Friend.friend import Friend
from slambook_restful.utils.custom_exceptions import ResourceAlreadyPresent


def save_new_friend(user, data):
    import pdb
    pdb.set_trace()
    is_duplicate = Friend.check_if_duplicate_friend(user, data)
    if is_duplicate:
        raise ResourceAlreadyPresent("Friend already exists with this email address")
    Friend.add_friend_details(user, data)


def add_new_friend_remote(bearer, data):
    is_duplicate = Friend.check_if_duplicate_friend(bearer, data)
    if is_duplicate:
        raise ResourceAlreadyPresent("Friend already exists with this email address")
    Friend.add_friend_details(bearer, data)
