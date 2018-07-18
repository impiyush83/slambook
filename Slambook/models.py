from string import lower

from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import String, and_
from sqlalchemy_wrapper import SQLAlchemy


db = SQLAlchemy('sqlite:///slambook.db')


class Parent(db.Model):
    __tablename__ = "parent"

    fn = db.Column(String)
    sn = db.Column(String)
    email = db.Column(String, primary_key=True)
    password = db.Column(String)
    gender = db.Column(String)
    childs = db.relationship('Child')



class Child(db.Model):
    __tablename__ = "child"
    email = db.Column(db.String, db.ForeignKey('parent.email'))
    friend = db.relationship("Parent")
    fn = db.Column(String)
    sn = db.Column(String)
    email = db.Column(String, primary_key=True)
    gender = db.Column(String)
    fcolor =db.Column(String)
    ffood = db.Column(String)
    fsong =db.Column(String)

db.create_all()



