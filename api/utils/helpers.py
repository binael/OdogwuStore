"""_summary_
"""
from urllib.parse import urlparse, urljoin
from flask import request

from api.models import Review

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
    