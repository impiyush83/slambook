from sqlalchemy import String, Integer

from slambook.extensions import db


class Test(db.Model):
    __tablename__ = "test"

    email = db.Column(String, unique=True)
    secret_key = db.Column(String, unique=True)
