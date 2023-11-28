"""_summary_
"""
from urllib.parse import urlparse, urljoin
from flask import request
from datetime import datetime

from api.models import Product
from api.models import Review
from api.models import Favorite
from api.models import Review

from api.utils.helper_class import MyRating

from api.utils.flaskforms import COUNTRY_CODES

def validate_url(url):
    """_summary_

	Args:
		url (_type_): _description_

	Returns:
		_type_: _description_
	"""
    base_url = urlparse(request.host_url)
    my_url = urlparse(urljoin(request.host_url, url))
    return my_url.scheme in ("http", "https") and base_url.netloc == my_url.netloc


def number_of_reviews(id):
    reviews = Review.query.filter_by(product_id=id).all()
    i = 0
    for review in reviews:
        i += 1

    return (i)


def isempty(name):
    """_summary_

	Args:
		name (_type_): _description_

	Returns:
		_type_: _description_
	"""
    if name == "" or name == None:
        return True
    return False


def seller_search(id, category, sub_category, name):
    products = []
    if isempty(category) and isempty(sub_category) and isempty(name):
        return Product.query.filter_by(id=id).all()


def get_product_rating(id):
    """_summary_

	Args:
		id (_type_): _description_

	Returns:
		_type_: _description_
	"""
    rated = Review.query.filter_by(product_id=id).all()
    total_rated = count = average_rated = 0
    for rates in rated:
        total_rated = rates.rating
        count += 1
    if count > 0:
        average_rated = total_rated / count
    return (count, average_rated)


def get_product_likes(id):
    """_summary_

	Args:
		id (_type_): _description_

	Returns:
		_type_: _description_
	"""
    likes = Favorite.query.filter_by(product_id=id).all()
    return len(likes)

def product_ratings(id):
    """_summary_

	Args:
		id (_type_): _description_

	Returns:
		_type_: _description_
	"""
    total_rating, average_rating = get_product_rating(id)
    likes = get_product_likes(id)
    return (MyRating(total_rating, average_rating, likes))


def cloudinary_public_id(image_file):
    """_summary_

	Args:
		image_file (_type_): _description_

	Returns:
		_type_: _description_
	"""
    if "o-store" not in image_file:
        return None
    url_list = image_file.split('/')
    index = url_list.index("o-store")
    return ("/".join(url_list[index:]))


def recent_added_query(user):
    """_summary_

	Args:
		user (_type_): _description_

	Returns:
		_type_: _description_
	"""
    q = Product.query.filter_by(seller_id=user.id)
    query = q.order_by(Product.updated_at.desc()).limit(12).all()
    return query


def get_address(full_address):
    """_summary_

	Args:
		full_address (_type_): _description_
		phone (_type_): _description_

	Returns:
		_type_: _description_
	"""
    address_list = full_address.split(',')
    country_name = address_list.pop().strip()
    country = ""
    for key, value in COUNTRY_CODES.items():
        if value.get("country").lower() == country_name.lower():
            country = key
            break
    state = address_list.pop().strip()
    city = address_list.pop().strip()
    street = ",".join(address_list)
    return {"country": country,
            "state": state,
            "city": city,
            "street": street
            }
