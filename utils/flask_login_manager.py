from functools import wraps

from flask import current_app, session
from flask_login import LoginManager, login_required, login_user, logout_user


class SmartLoginManager(LoginManager):
    """
    An app can have multiple registered instances
    of SmarterLoginManager for different User models,
    thus allowing for a simple authorization mechanism.

    Each view is required to be decorated with the
    appropriate manager's :method:`login_required`
    as follows:

        user_login_manager.login required
        def stats():
            return '', 200
    """

    def __init__(self, _name):
        self._name = _name
        self.session_protection = 'strong'
        super(SmartLoginManager, self).__init__()

    def login_required(self, func):
        login_required_func = login_required(func)

        @wraps(func)
        def decorated_view(*args, **kwargs):
            current_app.login_manager = self
            return login_required_func(*args, **kwargs)

        return decorated_view

    def login_user(self, *args):
        current_app.login_manager = self
        return login_user(*args)

    def logout_user(self):
        current_app.login_manager = self
        session.clear()
        return logout_user()

    def __str__(self):
        return 'SmarterLoginManager({})'.format(self._name)
