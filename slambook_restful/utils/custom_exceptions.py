class RequestValidationException(Exception):
    pass


class AuthenticationException(Exception):
    pass


class ResourceAlreadyPresent(Exception):
    pass


class ConflictState(Exception):
    pass
