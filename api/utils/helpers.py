"""_summary_
"""
from urllib.parse import urlparse, urljoin
from flask import request

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
