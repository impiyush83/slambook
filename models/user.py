from sqlalchemy import String

from app import db
from database import Base


class User(Base, db.Model):
    __tablename__ = "user"

    email = db.Column(String, unique=True)
    first_name = db.Column(String)
    last_name = db.Column(String)
    password = db.Column(String)
    gender = db.Column(String)
    childs = db.relationship('Friend')

