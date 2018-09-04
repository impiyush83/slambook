from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///slambook.db')



class Parent(db.Model):
    __tablename__ = "parent"

    fn = db.Column(db.String)
    sn = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    gender = db.Column(db.String)
    childs = db.relationship('Child')


class Child(db.Model):
    __tablename__ = "child"

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String, db.ForeignKey('parent.email'))
    friend = db.relationship("Parent")
    fn = db.Column(db.String)
    sn = db.Column(db.String)
    gender = db.Column(db.String)
    fcolor = db.Column(db.String)
    ffood = db.Column(db.String)
    fsong = db.Column(db.String)
    tel = db.Column(db.Integer)
    # image_path = db.Column(db.String)


class Secret(db.Model):
    __tablename__ = "secret"

    email = db.Column(db.String, db.ForeignKey('parent.email'), unique=True)
    secret_key = db.Column(db.String, primary_key=True)

db.create_all()
# Parent



