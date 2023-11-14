"""
A module that defines the model object for the database products
"""

from api import db
from api.models.base_model import BaseModel
from flask_login import UserMixin
from uuid import uuid4

class Seller(UserMixin, BaseModel):
    """
    A class for database product table
    """
    __tablename__ = "seller"
    id = db.Column(db.String(40), primary_key=True, nullable=False, default=str(uuid4()))
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    website = db.Column(db.String(120))
    phone = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(240))
    bio = db.Column(db.String(240))
    image = db.Column(db.String(240), nullable=False)

    products = db.relationship('Product', backref='sellers', lazy=True)

    def __init__(self, email, name, bio, image, website,
                 address, password, phone, firstname, lastname):
        self.email = email
        self.name = name
        self.bio = bio
        self.image = image
        self.website = website
        self.address = address
        self.password = password
        self.phone = phone
        self.firstname = firstname
        self.lastname = lastname

    def to_dict(self):
        """
        A function that returns database attributes in a dictionary
        format
        """
        my_dict = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "bio": self.bio,
            "image": self.image,
            "website": self.website,
            "address": self.address,
            "phone": self.phone
		}

        return my_dict

    def __repr__(self):
        """
        A string representation of database object
        """
        return "<{}(name: {})>".format(
            type(self).__name__, self.name
		)
