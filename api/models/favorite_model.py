"""
A module that defines the model object for the database products
"""

from api import db
from api.models.base_model import BaseModel


class Favorite(BaseModel):
    """
    A class for database product table
    """
    __tablename__ = "favorite"
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.String(40), db.ForeignKey("buyer.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
