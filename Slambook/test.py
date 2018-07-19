from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_wrapper import SQLAlchemy

db = SQLAlchemy('sqlite:///s.db')


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

    email = db.Column(db.String, ForeignKey('parent.email'))
    friend = db.relationship("Parent")
    fn = db.Column(db.String)
    sn = db.Column(db.String)
    gender = db.Column(db.String)
    fcolor = db.Column(db.String)
    ffood = db.Column(db.String)
    fsong = db.Column(db.String)
    image_path = db.Column(db.String,primary_key=True)

db.create_all()

p1 = Parent(fn="p",sn="p",email="p",password="p",gender="p")
db.add(p1)
db.commit()
c1 = Child(fn="wdqp",sn="pdqw",gender="wdqp",image_path="fwe",ffood = "wef" , fcolor="wfewe",fsong="fwef",friend=p1 )
c2 = Child(fn="wdqp",sn="pdqw",gender="wdqp",image_path="fwe",ffood = "wef" , fcolor="wfewe",fsong="fwef",friend=p1 )
print "1"
db.add(c1)
print "2"
db.add(c2)
print "3"
db.commit()
print "4"
obj = db.query(Parent).filter_by(fn="piyush").first()

# Parent
