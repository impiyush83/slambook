from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import Model

from extensions import db


class Parent(Model):
    __tablename__ = "parent"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    gender = Column(String)
    childs = relationship('Child')


class Child(Model):
    __tablename__ = "child"

    id = Column(Integer, primary_key=True)
    email = Column(String, ForeignKey('parent.email'))
    friend = relationship("Parent")
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    favourite_color = Column(String)
    favourite_food = Column(String)
    favourite_song = Column(String)
    tel = Column(Integer)


class Secret(Model):
    __tablename__ = "secret"

    email = Column(String, ForeignKey('parent.email'), unique=True)
    secret_key = Column(String, primary_key=True)


db.create_all()
