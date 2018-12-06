from sqlalchemy import String, Integer

from ..db import db


class Secret(db.Model):
    __tablename__ = "secret"

    id = db.Column(Integer, db.ForeignKey('user.id'), autoincrement=True, primary_key=True)
    email = db.Column(String, unique=True)
    secret_key = db.Column(String, unique=True)

    @classmethod
    def is_secret_key_created(cls, email):
        return db.query(cls).filter(cls.email == email).all()
