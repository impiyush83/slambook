from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///slambook.db')


class Parent(db.Model):
    __tablename__ = "parent"

    fn = Column(String)
    sn = Column(String)
    email = Column(String, primary_key=True)
    password = Column(String)
    gender = Column(String)
    childs = relationship('Child')


class Child(db.Model):
    __tablename__ = "child"
    email = Column(String, ForeignKey('parent.email'),primary_key=True)
    friend = relationship("Parent")
    fn = Column(String)
    sn = Column(String)
    gender = Column(String)
    fcolor = Column(String)
    ffood = Column(String)
    fsong = Column(String)
    image_path = Column(String)


db.create_all()
# Parent
