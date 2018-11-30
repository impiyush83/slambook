from sqlalchemy.dialects.postgresql import JSON

from app import db


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)

#
# class User(db.Model):
#     __tablename__ = "user"
#
#     email = db.Column(db.String, unique=True)
#     first_name = db.Column(db.String())
#     last_name = db.Column(db.String())
#     password = db.Column(db.String())
#     gender = db.Column(db.String())
#     childs = relationship('Friend')
#
#
# class Friend(db.Model):
#     __tablename__ = "friend"
#
#     email = db.Column(db.String(), ForeignKey('user.id'))
#     friend = relationship("User")
#     first_name = db.Column(db.String())
#     last_name = db.Column(db.String())
#     gender = db.Column(db.String())
#     favourite_color = db.Column(db.String())
#     favourite_food = db.Column(db.String())
#     favourite_song = db.Column(db.String())
#     mobile = db.Column(db.Integer)
#
#
# class Secret(db.Model):
#     __tablename__ = "secret"
#
#     email = db.Column(db.String, ForeignKey('user.id'), unique=True)
#     secret_key = db.Column(db.String, unique=True)
#
#
# class Secret5(db.Model):
#     __tablename__ = "secret5"
#
#     email = db.Column(db.String, ForeignKey('user.id'), unique=True)
#     secret_key = db.Column(db.String, unique=True)
#     secret_key_a = db.Column(db.String, unique=True)

