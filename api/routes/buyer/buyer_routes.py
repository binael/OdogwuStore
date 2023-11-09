"""
"""

from flask import Blueprint, render_template

buyer = Blueprint("buyer", __name__,
                 template_folder="templates",
                 static_folder="static",
                 static_url_path="/")

@buyer.route("/", strict_slashes=False)
@buyer.route("/home", strict_slashes=False)
def homepage():
    return render_template("home.html")

@buyer.route("/search", strict_slashes=False)
def searchkeyword():
    return render_template("search.html")
