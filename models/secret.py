from sqlalchemy import String, Integer

from app import db


class Secret(db.Model):
    __tablename__ = "secret"

    id = db.Column(Integer, db.ForeignKey('user.id'), autoincrement=True, primary_key=True)
    email = db.Column(String, unique=True)
    secret_key = db.Column(String, unique=True)
