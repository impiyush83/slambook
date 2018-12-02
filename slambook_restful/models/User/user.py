from sqlalchemy import String

from slambook.extensions import db
from slambook_restful.models.Base import Base


class User(Base, db.Model):
    __tablename__ = "user"

    email = db.Column(String, unique=True,  nullable=False)
    first_name = db.Column(String, nullable=False)
    last_name = db.Column(String,  nullable=False)
    password = db.Column(String,  nullable=False)
    gender = db.Column(String,  nullable=False)
    childs = db.relationship('Friend')

    @classmethod
    def insert_user(cls, first_name, last_name, email, password, gender):
        u1 = cls(first_name=first_name, last_name=last_name, email=email, password=password, gender=gender)
        db.add(u1)
        db.flush()
        db.commit()

