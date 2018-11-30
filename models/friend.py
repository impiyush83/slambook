from sqlalchemy import Integer, String
from app import db


class Friend(db.Model):
    __tablename__ = "friend"

    id = db.Column(Integer, db.ForeignKey('user.id'), autoincrement=True, primary_key=True)
    email = db.Column(String)
    friend = db.relationship("User")
    first_name = db.Column(String)
    last_name = db.Column(String)
    gender = db.Column(String)
    favourite_color = db.Column(String)
    favourite_food = db.Column(String)
    favourite_song = db.Column(String)
    mobile = db.Column(db.Integer)
