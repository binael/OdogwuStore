"""
"""

from api.utils.flaskforms import AddProduct

from flask import Blueprint, render_template

seller = Blueprint("seller", __name__,
                        template_folder="templates",
                        static_folder="static",
                        static_url_path="/",
                        url_prefix="/o-sellers")

@seller.route("/", strict_slashes=False)
def home():
    return render_template("home.html")
