from _operator import and_

from sqlalchemy import Integer, String

from slambook_restful.models.db import db


class Friend(db.Model):
    __tablename__ = "friend"
    user_id = db.Column(Integer, db.ForeignKey('user.id'))
    id = db.Column(Integer, autoincrement=True, primary_key=True)
    email = db.Column(String, nullable=False)
    friend = db.relationship("User")
    first_name = db.Column(String)
    last_name = db.Column(String)
    gender = db.Column(String)
    favourite_color = db.Column(String)
    favourite_food = db.Column(String)
    favourite_song = db.Column(String)
    mobile = db.Column(db.String)

    @classmethod
    def get_friends_with_email_address(cls, user_id):
        return db.query(cls).filter(cls.user_id == user_id).all()

    @classmethod
    def add_friend_details(cls, user, data):
        friend = cls(user_id=user.id, email=data.get("email"), first_name=data.get("first_name"),
                     last_name=data.get("last_name"),
                     mobile=data.get("mobile"), favourite_food=data.get("favourite_food"), gender=data.get("gender"),
                     favourite_song=data.get("favourite_song"), favourite_color=data.get("favourite_color"))
        db.session.add(friend)
        db.flush()

    @classmethod
    def check_if_duplicate_friend(cls, user, data):
        return db.query(cls).filter(and_(cls.user_id == user.id, cls.email == data.get("email"))).first()

    @classmethod
    def check_if_current_user(cls, user, data):
        return db.query(cls).filter(and_(cls.user_id == user.id, cls.email == user.email)).first()
