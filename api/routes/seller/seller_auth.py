"""
"""

from flask import Blueprint, render_template

seller_auth = Blueprint("seller_auth", __name__,
                        template_folder="templates",
                        static_folder="static",
                        static_url_path="/",
                        url_prefix="/o-sellers")

@seller_auth.route("/login", strict_slashes=False)
def login():
    return render_template("home.html")
