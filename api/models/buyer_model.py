"""
A module that defines the model object for the database products
"""

from api import db
from api.models.base_model import BaseModel
from flask_login import UserMixin
from uuid import uuid4


class Buyer(UserMixin, BaseModel):
    """
    A class for database product table
    """
    __tablename__ = "buyer"
    id = db.Column(db.String(40), primary_key=True, nullable=False, default=str(uuid4()))
    firstname = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(30), unique=True, nullable=False)
    address = db.Column(db.String(240))
    image = db.Column(db.String(240))

    favorites = db.relationship("Favorite", backref="buyers", lazy=True)
    purchases = db.relationship("Purchase", backref="buyers", lazy=True)


    def __init__(self, email, firstname, lastname, phone, address, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.password = password
        self.address = address

    def to_dict(self):
        """
        A function that returns database attributes in a dictionary
        format
        """
        my_dict = {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "phone": self.phone,
            "address": self.address
		}

        return my_dict

    def __repr__(self):
        """
        A string representation of database object
        """
        return "<{}(name: {})>".format(
            type(self).__name__, (self.firstname + ' ' + self.lastname)
		)
