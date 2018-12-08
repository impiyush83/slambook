from slambook_restful.models.Secret.secret import Secret


def save_secret_key(user, secret_key):
    Secret.add_to_db(id=user.id, email=user.email, secret_key=secret_key)


def get_secret_key(list_of_secret_keys):
    if list_of_secret_keys:
        secret_key = list_of_secret_keys[0].secret_key
    else:
        secret_key = None
    return secret_key
