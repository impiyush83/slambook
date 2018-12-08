from flask_jwt_extended import get_jwt_identity

from slambook_restful.models.Secret.secret import Secret
from slambook_restful.models.User.user import User
from slambook_restful.utils.custom_exceptions import ConflictState, NoResultFound
from slambook_restful.views.friend import add_new_friend_remote


def transfer_profile(data):
    try:
        bearer_id = Secret.get_user_id_from_secret_key(data.get("secret_key"))
    except:
        raise NoResultFound("Secret Key doesn't matches")
    bearer = User.with_id(bearer_id)
    user_id = get_jwt_identity()
    user = User.with_id(user_id)
    if user_id == bearer_id:
        raise ConflictState("Un haan !! Its your secret key !! Try with your friends secret key !! ")
    data = {'first_name': user.first_name , 'last_name': user.last_name, 'gender': user.gender,
            'favourite_color': user.favourite_color, 'favourite_food': user.favourite_food,
            'favourite_song': user.favourite_song, 'mobile': user.mobile, 'email': user.email}
    add_new_friend_remote(bearer, data)

