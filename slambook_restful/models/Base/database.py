import inflection
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declared_attr

from slambook_restful.manage import db

Model = db.Model


class SurrogatePK(object):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, autoincrement=True, primary_key=True)


class HasTablename(object):
    @declared_attr
    def __tablename__(cls):
        return inflection.underscore(cls.__name__)


class Base(HasTablename, SurrogatePK):
    def update_attributes(self, dict):
        for name, value in list(dict.items()):
            setattr(self, name, value)

    def __repr__(self):
        return '<{model}({id})>'.format(model=self.__class__.__name__, id=self.id)

