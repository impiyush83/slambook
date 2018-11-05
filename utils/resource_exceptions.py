from functools import wraps
from flask_restful import abort
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.exceptions import HTTPException
from flask import current_app as app, make_response
from utils.custom_exceptions import \
    RequestValidationException, AuthenticationException, \
    ResourceAlreadyPresent, ConflictState


def exception_handle(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except RequestValidationException as val_err:
            app.logger.error(val_err)
            db.rollback()
            return abort(make_response(val_err.args[0], 400))
        except NoResultFound as val_err:
            app.logger.error(val_err)
            db.rollback()
            return abort(400, message=str(val_err))
        except ValueError as val_err:
            app.logger.error(val_err)
            db.rollback()
            return abort(400, message=str(val_err))
        except AuthenticationException as e:
            app.logger.error(e)
            db.rollback()
            return abort(401, message=str(e))
        except HTTPException as e:
            app.logger.error(e)
            db.rollback()
            return abort(e.code, message=e.description)
        except KeyError as key_err:
            app.logger.error(key_err)
            db.rollback()
            return abort(400, message=str(key_err))
        except IOError as io_err:
            app.logger.error()
            db.rollback()
            return abort(403, message=str(io_err))
        except ResourceAlreadyPresent as exc:
            app.logger.error(exc)
            db.rollback()
            return abort(409, message=str(exc))
        except ConflictState as exc:
            app.logger.error(exc)
            db.rollback()
            return abort(409, message=str(exc))
        except Exception as exc:
            app.logger.error(exc)
            db.rollback()
            return abort(500, message=str(exc))

    return wrapper
