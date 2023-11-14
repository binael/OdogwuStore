"""
A module containing objects for all db models that will be created
"""

from api import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class BaseModel(db.Model):
    """
    A class containing methods and attributes that will be shared
    by all models

    Parameters:
    -----------
    """
    __abstract__ = True

    created_at = db.Column(db.DateTime(), default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime(), default=datetime.now, nullable=False)

    def add(self):
        """
        """
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
        """
        updated_at = datetime.now()
        db.session.commit()

    def delete(self):
        """
        """
        db.session.delete(self)
        db.session.commit()
