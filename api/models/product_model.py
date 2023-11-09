"""
A module that defines the model object for the database products
"""

from uuid import uuid4
import re

from api import db
from api.models.base_model import BaseModel


class Product(BaseModel):
    """
    A class for database product table
    """
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    link = db.Column(db.String(120))
    seller_id = db.Column(db.String(40), db.ForeignKey('seller.id'))
    category = db.Column(db.String(80), nullable=False)
    sub_category = db.Column(db.String(240), nullable=False)
    name = db.Column(db.String(480), nullable=False)
    total_stock = db.Column(db.Integer, nullable=False)
    stock_remaining = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(600), nullable=False)
    image = db.Column(db.String(120), nullable=False)

    favorites = db.relationship("Favorite", backref="products", lazy=True)
    purchases = db.relationship("Purchase", backref="products", lazy=True)

    def __init__(self, category, sub_category, name, total_stock,
                 stock_remaining, price, description, image,
                 discount=0):
        """
        Instance variables
        """
        self.category = category
        self.name = name
        self.total_stock = total_stock
        self.price = price
        self.discount = discount
        self.description = description
        self.image = image
        self.stock_remaining = stock_remaining

        # Set the value of self.id
        p_array = name.split(' ')
        total = 0
        for i in len(p_array):
            total = len(p_array[i])
            if (i >= 6) or (total > 100):
                break
        if total > 100:
            i = i - 1
        for j in range(i):
            self.link = p_array + '-'
        self.link = self.link + str(uuid4())[-7:]

        # Format sub-category
        catRegex = re.findall(r'[a-zA-Z]+', sub_category)
        self.sub_category = ""
        i = 0
        for word in catRegex:
            if word == "s":
                continue
            if i >= 1:
                self.sub_category += "-" + word
            else:
                self.sub_category += word
            i += 1

    def to_dict(self):
        """
        A function that returns database attributes in a dictionary
        format
        """
        my_dict = {
            "id": self.id,
            "link": self.link,
            "name": self.name,
            "category": self.category,
            "discount": self.discount,
            "price": self.price,
            "total_stock": self.total_stock,
            "remaining_stock": self.stock_remaining,
            "image": self.image,
            "description": self.description
		}
        sub_category = self.sub_category
        my_dict["sub_category"] = sub_category.replace("-", " ")
        return my_dict

    def __repr__(self):
        """
        A string representation of database object
        """
        return "<{}(name: {})>".format(
            type(self).__name__, self.name
		)
