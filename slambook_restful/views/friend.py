from slambook_restful.models.Friend.friend import Friend


def save_new_friend(user, data):
    Friend.add_friend_details(user, data)
