"""
"""

from flask import Blueprint, render_template

from api.utils.flaskforms import SubscribeForm

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
    return render_template("search.html")
