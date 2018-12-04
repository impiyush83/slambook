from sqlalchemy import String

from ..db import db
from slambook_restful.models.Base.database import Base


class User(Base, db.Model):
    __tablename__ = "user"

    email = db.Column(String, unique=True,  nullable=False)
    first_name = db.Column(String, nullable=False)
    last_name = db.Column(String,  nullable=False)
    password = db.Column(String,  nullable=False)
    gender = db.Column(String,  nullable=False)
    childs = db.relationship('Friend')

    @classmethod
    def insert_user(cls, user_obj):
        u1 = cls(first_name=user_obj.get("first_name"), last_name=user_obj.get("last_name"),
                 email=user_obj.get("email"), password=user_obj.get("password"), gender=user_obj.get("gender"))
        db.add(u1)
        db.flush()
        db.commit()

