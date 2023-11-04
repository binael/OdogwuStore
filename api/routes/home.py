"""
"""

from flask import Blueprint, render_template, url_for

home = Blueprint("home", __name__,
                 template_folder="templates")

@home.route("/", strict_slashes=False)
@home.route("/home", strict_slashes=False)
def homepage():
    return render_template("home.html")
