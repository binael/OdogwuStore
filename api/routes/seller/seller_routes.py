"""
"""

from api.utils.flaskforms import SellerSearchForm, SubscribeForm, AddProductForm

from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

seller = Blueprint("seller", __name__,
                        template_folder="templates",
                        static_folder="static",
                        static_url_path="/",
                        url_prefix="/o-seller")

@seller.route("/", strict_slashes=False, methods=['GET', 'POST'])
@login_required
def homepage():
    form = SellerSearchForm()
    subscribe = SubscribeForm()

    if form.validate_on_submit() and request.method == "POST":
        return render_template("homePage.html", form=form, subscribe=subscribe, firstname=current_user.firstname.title())
    return render_template("homePage.html",
                           form=form,
                           subscribe=subscribe,
                           user=current_user
                           )


@seller.route("/add", strict_slashes=False, methods=['GET', 'POST'])
@login_required
def add():
    form = SellerSearchForm()
    subscribe = SubscribeForm()
    add_product_form = AddProductForm()

    return render_template("addProduct.html",
                           form=form,
                           subscribe=subscribe,
                           add_product_form=add_product_form,
                           user=current_user
                           )
