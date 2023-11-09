"""
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, TextAreaField, DecimalField
from wtforms.validators import InputRequired, NumberRange


class AddProduct(FlaskForm):
    """
    
    """
    category = StringField("Product Category")
    sub_category = StringField("Sub Category")
    name = StringField("Product Name")
    total_stock = IntegerField("Quantity in Stock")
    price = DecimalField('Product Price', places=2, validators=[NumberRange(min=0.01)])
    discount = IntegerField("Discount", validators=[NumberRange(min=0, max=99)])
    description = StringField("Product Description")
    image = FileField("Image")
