from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

session = None
session_obj = None


def get_session_obj(database_url):
    global session_obj
    session_obj = sessionmaker(bind=create_engine(database_url))
    return session_obj


def get_session(database_url=None):
    global session
    global session_obj
    if session:
        return session

    if not session_obj:
        session_obj = get_session_obj(database_url)
    session = scoped_session(session_obj)
    return session
