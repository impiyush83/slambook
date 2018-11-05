from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import Model

from database import Base


class User(Base, Model):
    __tablename__ = "user"

    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    gender = Column(String)
    childs = relationship('Friend')


class Friend(Base, Model):
    __tablename__ = "child"

    email = Column(String, ForeignKey('user.email'))
    friend = relationship("User")
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    favourite_color = Column(String)
    favourite_food = Column(String)
    favourite_song = Column(String)
    tel = Column(Integer)


class Secret(Base, Model):
    __tablename__ = "secret"

    email = Column(String, ForeignKey('user.id'), unique=True)
    secret_key = Column(String, unique=True)


db.create_all()
