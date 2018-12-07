from slambook_restful.models.Secret.secret import Secret


def save_secret_key(user, secret_key):
    Secret.add_to_db(email=user.email, secret_key=secret_key)
