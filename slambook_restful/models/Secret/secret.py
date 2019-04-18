from sqlalchemy import String, Integer

from ..db import db


class Secret(db.Model):
    __tablename__ = "secret"

    id = db.Column(Integer, db.ForeignKey('user.id'))
    email = db.Column(String, unique=True)
    secret_key = db.Column(String, unique=True, primary_key=True)

    @classmethod
    def is_secret_key_created(cls, email):
        return db.query(cls).filter(cls.email == email).all()

    @classmethod
    def insert(cls, id, email, secret_key):
        db.session.add(cls(id=id, email=email, secret_key=secret_key))
        db.flush()

    @classmethod
    def get_user_id_from_secret_key(cls, secret_key):
        secret_object = db.query(cls).filter(cls.secret_key == secret_key).first()
        return secret_object.id
