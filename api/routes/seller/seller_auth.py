"""
"""

from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from cloudinary.uploader import upload

from api.utils.flaskforms import SellerLoginForm, SubscribeForm, SellerSignUpForm
from api.utils.flaskforms import COUNTRY_CODES
from api.models import Seller

seller_auth = Blueprint("seller_auth", __name__,
                        template_folder="templates",
                        static_folder="static",
                        static_url_path="/",
                        url_prefix="/o-seller")

@seller_auth.route("/login", strict_slashes=False, methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("seller.homepage"))

    form = SellerLoginForm()
    subscribe = SubscribeForm()

    if request.method == "POST" and form.validate_on_submit():
        user = Seller.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            session["role"] = "seller"
            return redirect(url_for("seller.homepage"))
        return render_template("loginPage.html", form=form, subscribe=subscribe, name=True)

    if request.method == "POST" and subscribe.validate_on_submit():
        return redirect(url_for('seller_auth.login'))

    return render_template("loginPage.html", form=form, subscribe=subscribe)

@seller_auth.route("/sign_up", strict_slashes=False, methods=["GET", "POST"])
def sign_up():
    """_summary_
	"""
    subscribe = SubscribeForm()
    form = SellerSignUpForm()
    if request.method == "POST" and form.validate_on_submit():
        user = Seller.query.filter_by(email=form.email.data.lower()).first()
        if user:
            return "This seller email already exists"
        full_address = form.address.street.data + ', '
        full_address += form.address.city.data + ', '
        full_address += form.address.state.data + ', '
        full_address += COUNTRY_CODES.get(form.address.country.data).get("country").title()

        upload_result = upload(form.image.data, folder="/o-store/seller")
        image_file = upload_result["secure_url"]

        firstname = form.firstname.data.lower()
        lastname = form.lastname.data.lower()
        email = form.email.data.lower()

        user = Seller(firstname=firstname, lastname=lastname,
                      email=email, name=form.name.data,
                      phone=form.address.phone.data, bio=form.bio.data,
                      website=form.website.data, address=full_address,
                      password=generate_password_hash(form.password.password.data),
                      image=image_file
		)
        user.add()
        return redirect(url_for("seller_auth.login"))
    if request.method == "POST" and subscribe.validate_on_submit():
        return redirect(url_for('seller_auth.login'))
    return render_template("signPage.html", form=form, subscribe=subscribe)

@seller_auth.route("/logout", strict_slashes=False, methods=["GET", "POST"])
# @login_required
def logout():
    """
    """
    logout_user()
    return redirect(url_for('seller_auth.login'))


@seller_auth.route("/forgot_password", strict_slashes=False, methods=["GET", "POST"])
def forgot_password():
    return "Implementation coming up"
