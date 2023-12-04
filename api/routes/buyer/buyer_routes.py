"""
"""

from flask import Blueprint, render_template

from api.utils.flaskforms import SubscribeForm

from api.utils.helpers import discount_price

from api.service import search_a_product
from api.service.search import CATEGORY

buyer = Blueprint("buyer", __name__,
                 template_folder="templates",
                 static_folder="static",
                 static_url_path="/")

@buyer.route("/", strict_slashes=False, methods=["GET", "POST"])
@buyer.route("/home", strict_slashes=False, methods=["GET", "POST"])
def homepage():
    subscribe = SubscribeForm()
    return render_template("home.html", subscribe=subscribe)

@buyer.route("/search", strict_slashes=False)
def searchkeyword():
    subscribe = SubscribeForm()
    return render_template("search.html", subscribe=subscribe)

@buyer.route("/<name>", strict_slashes=False)
def product(name):
    subscribe = SubscribeForm()
    new = []
    products = search_a_product(name)
    if isinstance(products, list):
        search_text = f"Category - {CATEGORY.get(name).title()}"
        return render_template("search.html",
                               subscribe=subscribe,
                               products=products,
                               search_text=search_text,
                               discount_price=discount_price)
    else:
        search_text = f"Search Results - {name.title()}"
        return render_template("search.html",
                               subscribe=subscribe,
                               products=products,
                               search_text=search_text)
