from sqlalchemy import String

from slambook_restful.models.Base.database import Base
from slambook_restful.utils.utils import encrypt_password
from ..db import db


class User(Base, db.Model):
    __tablename__ = "user"

    email = db.Column(String, unique=True, nullable=False)
    first_name = db.Column(String, nullable=False)
    last_name = db.Column(String, nullable=False)
    password = db.Column(String, nullable=False)
    gender = db.Column(String, nullable=False)
    childs = db.relationship('Friend')

    @classmethod
    def insert_user(cls, user_obj):
        encrypted_password = encrypt_password(user_obj.get("password"))
        u1 = cls(first_name=user_obj.get("first_name"), last_name=user_obj.get("last_name"),
                 email=user_obj.get("email"), password=encrypted_password, gender=user_obj.get("gender"))
        db.session.add(u1)
        db.flush()
        db.commit()

    @classmethod
    def with_email_address(cls, email):
        return db.query(User).filter(User.email == email).first()

    @classmethod
    def with_id(cls, id):
        return db.query(User).filter(User.id == id).first()
