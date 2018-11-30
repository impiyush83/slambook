from sqlalchemy import String, Integer
from sqlalchemy_wrapper import Model
from app import db


class Secret(Model):
    __tablename__ = "secret"

    id = db.Column(Integer, db.ForeignKey('user.id'), autoincrement=True, primary_key=True)
    email = db.Column(String, db.ForeignKey('user.id'), unique=True)
    secret_key = db.Column(String, unique=True)
