"""_summary_
"""
from PIL import Image

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (StringField, IntegerField, TelField,
                     TextAreaField, DecimalField, SearchField,
                     SelectField, EmailField, PasswordField,
                     BooleanField, FormField)
from wtforms.validators import InputRequired, NumberRange, Length, EqualTo, ValidationError

ALL_CATEGORY = [
    ("none", "None"), ("appliances", "Appliances"),
    ("computer and accessories", "Computer and Accessories"), ("fashion", "Fashion"),
    ("furniture", "Furniture"), ("games and toys", "Games and Toys"),
    ("groceries", "Groceries"), ("health and beauty", "Health and Beauty"),
    ("home and office", "Home and Office"), ("jewelries and watches", "Jewelries and Watches"),
    ("phones and tablets", "Phones and Tablets"), ("other categories", "Other Categories")
]

# Country Codes to 
COUNTRY_CODES = {
    "ng": {"country": "nigeria",
           "currency_code": "NGN",
           "currency": "Naira (NGN)",
		   "rate": 802.11
		   },
    "us": {"country": "united states",
           "currency_code": "USD",
           "currency": "Dollar (USD)",
		   "rate": 1
		   },
    "gh": {"country": "ghana",
           "currency_code": "GHS",
           "currency": "Cedi (GHS)",
		   "rate": 11.88
		   },
    "ca": {"country": "canada",
           "currency_code": "CAD",
           "currency": "Dollar (CAD)",
		   "rate": 1.38
		   },
    "gb": {"country": "united kingdom",
           "currency_code": "GBP",
           "currency": "Pound Sterling (GBP)",
		   "rate": 0.81
		   },
    "fr": {"country": "france",
           "currency_code": "EUR",
           "currency": "Euro (EUR)",
		   "rate": 0.93
		   },
    "sa": {"country": "south africa",
           "currency_code": "ZAR",
           "currency": "Rand (ZAR)",
		   "rate": 18.95
		   },
    "rw": {"country": "rwanda",
           "currency_code": "RWF",
           "currency": "Franc (RWF)",
           "rate": 1228
           }
}

COUNTRY = [(key, value.get("country")) for key, value in COUNTRY_CODES.items()]
CURRENCY = [(value.get("currency_code"), value.get("currency")) for value in COUNTRY_CODES.values()]

class SubscribeForm(FlaskForm):
    """_summary_

	Args:
		FlaskForm (_type_): _description_
	"""
    email = EmailField('Email', validators=[InputRequired()])


class SellerSearchForm(FlaskForm):
    """_summary_

	Args:
		FlaskForm (_type_): _description_
	"""
    sub_category = StringField("Sub Category")
    product = SearchField("Product Name")
    category = SelectField("Category", choices=ALL_CATEGORY)


class SellerLoginForm(FlaskForm):
    """_summary_

	Args:
		FlaskForm (_type_): _description_
	"""
    email = EmailField("EMAIL ADDRESS", validators=[InputRequired()])
    password = PasswordField("PASSWORD", validators=[InputRequired(), Length(min=6, max=16)])
    remember_me = BooleanField('Remember Me')


class AddressForm(FlaskForm):
    """_summary_

	Args:
		FlaskForm (_type_): _description_
	"""
    country = SelectField("Country", choices=COUNTRY)
    state = StringField("State", validators=[InputRequired()])
    city = StringField("Street", validators=[InputRequired()])
    street = StringField("Street", validators=[InputRequired()])
    phone = TelField("Phone", validators=[InputRequired()])


class ChangePasswordForm(FlaskForm):
    """_summary_

	Args:
		FlaskForm (_type_): _description_
	"""
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6, max=16)])
    confirm = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo("password", message="Passwords are not the same")])


class SellerSignUpForm(FlaskForm):
    """_summary_

	Args:
		FlaskForm (_type_): _description_
	"""
    firstname = StringField("First Name", validators=[InputRequired()])
    lastname = StringField("Last Name", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired()])
    name = StringField("Company Name", validators=[InputRequired()])
    website = StringField("Website")
    address = FormField(AddressForm)
    bio = TextAreaField("Bio", validators=[InputRequired()])
    password = FormField(ChangePasswordForm)
    image = FileField("Image", validators=[FileRequired() ,FileAllowed(['jpg', 'png', 'gif', 'jfif', 'webp', 'bmp', 'jpeg'])])


class AddProductForm(FlaskForm):
    """_summary_

	Args:
		FlaskForm (_type_): _description_
	"""
    category = SelectField("Category", choices=ALL_CATEGORY[1:])
    sub_category = StringField("Sub Category", validators=[InputRequired()])
    name = StringField("Product Name", validators=[InputRequired()])
    total_stock = IntegerField("Total Stock", validators=[InputRequired(), NumberRange(min=1)])
    stock_remaining = IntegerField("Stock Remaining")
    currency = SelectField("Currency", choices=CURRENCY)
    price = DecimalField('Product Price', places=2, validators=[InputRequired(), NumberRange(min=0.01)])
    discount = IntegerField("Discount", default=0, validators=[InputRequired() ,NumberRange(min=0, max=99)])
    description = TextAreaField("Product Description", validators=[InputRequired()])
    image = FileField("Image", validators=[FileRequired() ,FileAllowed(['jpg', 'png', 'gif', 'jfif', 'webp', 'bmp', 'jpeg'])])

    def validate_image(self, field):
        """_summary_

		Args:
			field (_type_): _description_

		Raises:
			ValidationError: _description_

		Returns:
			_type_: _description_
		"""
        size = 1024 * 1024 * 1  # 1MB maximum value
        try: 
            with Image.open(field.data.filename) as img:
                width, height = img.size
                if width * height > size:
                    raise ValidationError("Image File Size Must Not Exceed 1MB")
        except (OSError, FileNotFoundError, IOError):
            return ValidationError("Not a Valid Image File")

    def validate_price(self, field):
        """_summary_

		Args:
			field (_type_): _description_

		Raises:
			ValidationError: _description_
		"""
        price = str(field.data)
        price = price.split('.')
        if len(price) == 2 and not (len(price[-1]) <= 2):
            raise ValidationError("Error: More Than Two Decimal Places")
