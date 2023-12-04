"""
"""

# Test modules
# import requests as req
# from api.utils.flaskforms import ALL_CATEGORY
# from random import randint
# from api import db
# from sqlalchemy import text

from api.utils.flaskforms import SellerSearchForm, SubscribeForm, AddProductForm
from api.utils.flaskforms import UpdateProductForm, ProfileForm, ContactForm
from api.utils.flaskforms import COUNTRY_CODES

from api.utils.helpers import cloudinary_public_id
from api.utils.helpers import seller_search, product_ratings
from api.utils.helpers import recent_added_query, get_address

from api.models import Product
from api.models import Seller
from api.models import Review
from api.models import Purchase

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash

from cloudinary.uploader import upload, destroy
from cloudinary.utils import cloudinary_url

from api.service import subscribe_mail, contact_us_mail
from api.service import search_product

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

    # objects from db
    products = Product.query.filter_by(seller_id=current_user.id).all()

    if subscribe.validate_on_submit() and request.method == 'POST':
        subscribe_mail([subscribe.email.data])
        return redirect(url_for("seller.homepage"))

    if form.validate_on_submit() and request.method == "POST":
        products = search_product(id=current_user.id,
                                  category=form.category.data,
                                  product=form.product.data)
        return render_template("homePage.html",
                               form=form,
                               subscribe=subscribe,
                               user=current_user,
                               products=products
                               )

    return render_template("homePage.html",
                           form=form,
                           subscribe=subscribe,
                           user=current_user,
                           products=products
                           )

@seller.route("/add", strict_slashes=False, methods=['GET', 'POST'])
@login_required
def add():
    subscribe = SubscribeForm()
    form = AddProductForm()

    if form.validate_on_submit() and request.method == "POST":
        image_file = form.image.data
        upload_result = upload(image_file, folder="o-store/product")
        image_file, options = cloudinary_url(upload_result["public_id"])

        product = Product(name=form.name.data, price=form.price.data,
                          category=form.category.data, sub_category=form.sub_category.data,
                          total_stock=form.total_stock.data, discount=form.discount.data,
                          stock_remaining=form.total_stock.data, image=image_file,
                          currency=form.currency.data, description=form.description.data
                          )
        product.seller_id=current_user.id
        product.add()
        flash("Product Successfully Added")
        return render_template("addProduct.html",
                               form=form,
                               subscribe=subscribe,
                               user=current_user,
                               product=product)

    if subscribe.validate_on_submit() and request.method == 'POST':
        subscribe_mail([subscribe.email.data])
        return redirect(url_for("seller.add"))

    return render_template("addProduct.html",
                           form=form,
                           subscribe=subscribe,
                           user=current_user
                           )


@seller.route("/<link>", strict_slashes=False, methods=['GET', 'POST'])
@login_required
def product(link):
    """_summary_

	Args:
		link (_type_): _description_

	Returns:
		_type_: _description_
	"""
    product = Product.query.filter_by(link=link).first()
    # forms
    subscribe = SubscribeForm()
    form = UpdateProductForm(obj=product)
    rating = []
    if product:
        rating = product_ratings(product.id)
    # Validate Subscribe form
    if subscribe.validate_on_submit() and request.method == 'POST':
        subscribe_mail([subscribe.email.data])
        return redirect(url_for("seller.product", link=product.link))

    if form.validate_on_submit() and request.method == "POST":
        # Delete image from cloudinary database
        public_id = cloudinary_public_id(product.image)
        if public_id:
            destroy(public_id)
        # Get the input image details from the form and upload
        image_file = form.image.data
        if image_file:
            upload_result = upload(image_file, folder="o-store/product")
            image_file, options = cloudinary_url(upload_result["public_id"])
        # Update details of the database
        product.image = image_file
        product.price = form.price.data
        product.stock_remaining = form.stock_remaining.data
        product.discount = form.discount.data
        product.update()
        # Redirect back to the url
        return redirect(url_for("seller.product", link=product.link))
    return render_template("productPage.html",
                           subscribe=subscribe,
                           product=product,
                           user=current_user,
                           form=form,
                           rating=rating)


@seller.route("/recently_added", strict_slashes=False, methods=['GET', 'POST'])
@login_required
def recently_added():
    """_summary_

	Returns:
		_type_: _description_
	"""
    form = SellerSearchForm()
    subscribe = SubscribeForm()
    # objects from db
    products = recent_added_query(current_user)
    if form.validate_on_submit() and request.method == "POST":
        products = seller_search(id=current_user.id,
                                 category=form.category.data,
                                 sub_category=form.sub_category.data,
                                 name=form.product.data)
        return render_template("recentlyAdded.html",
                               form=form,
                               subscribe=subscribe,
                               user=current_user,
                               products=products
                               )

    if subscribe.validate_on_submit() and request.method == 'POST':
        subscribe_mail([subscribe.email.data])
        return redirect(url_for("seller.recently_added"))

    return render_template("recentlyAdded.html",
                           form=form,
                           subscribe=subscribe,
                           user=current_user,
                           products=products
                           )

@seller.route("/profile", strict_slashes=False, methods=["GET", "POST"])
@login_required
def profile():
    """_summary_

	Returns:
		_type_: _description_
	"""
    # Get the profile object
    subscribe = SubscribeForm()
    profile = ProfileForm(obj=current_user)
    # Populate profile Address data
    address = get_address(current_user.address)
    profile.address.phone.data = current_user.phone
    profile.address.country.data = address.get("country")
    profile.address.state.data = address.get("state")
    profile.address.city.data = address.get("city")
    profile.address.street.data = address.get("street")
    # Resolve Post Request for profile form
    if request.method == "POST" and profile.validate_on_submit():
        full_address = profile.address.street.data + ', '
        full_address += profile.address.city.data + ', '
        full_address += profile.address.state.data + ', '
        full_address += COUNTRY_CODES.get(profile.address.country.data).get("country").title()
        # Delete image from cloudinary database
        try:
            public_id = cloudinary_public_id(current_user.image)
            if public_id:
                destroy(public_id)
        except Exception:
            pass
        # Get the input image details from the profile and upload
        image_file = profile.image.data
        if image_file:
            upload_result = upload(image_file, folder="o-store/seller")
            image_file, options = cloudinary_url(upload_result["public_id"])
        # Update details of the database
        firstname = profile.firstname.data.title()
        lastname = profile.lastname.data.title()
        email = profile.email.data.lower()

        user = current_user
        user.firstname = firstname 
        user.lastname = lastname
        user.email = email
        user.name = profile.name.data
        user.phone = profile.address.phone.data
        user.bio = profile.bio.data
        user.website=profile.website.data
        user.address=full_address
        user.image=image_file

        user.update()
        flash("Account Successfully Updated")
        return redirect(url_for("seller.profile"))

    if subscribe.validate_on_submit() and request.method == 'POST':
        subscribe_mail([subscribe.email.data])
        return redirect(url_for('seller.profile'))
    return render_template("profilePage.html", profile=profile, subscribe=subscribe, user=current_user)

@seller.route("/faq", strict_slashes=False, methods=["GET", "POST"])
def faq():
    """_summary_

	Returns:
		_type_: _description_
	"""
    subscribe = SubscribeForm()
    if subscribe.validate_on_submit() and request.method == 'POST':
        subscribe_mail([subscribe.email.data])
        return redirect(url_for('seller.faq'))
    return render_template("faqPage.html", subscribe=subscribe)

@seller.route("/about", strict_slashes=False, methods=["GET", "POST"])
def about():
    """_summary_

	Returns:
		_type_: _description_
	"""
    subscribe = SubscribeForm()
    if subscribe.validate_on_submit() and request.method == 'POST':
        subscribe_mail([subscribe.email.data])
        return redirect(url_for('seller.about'))
    return render_template("aboutPage.html", subscribe=subscribe)

@seller.route("/office", strict_slashes=False, methods=["GET", "POST"])
def office():
    """_summary_

	Returns:
		_type_: _description_
	"""
    subscribe = SubscribeForm()
    if subscribe.validate_on_submit() and request.method == 'POST':
        subscribe_mail([subscribe.email.data])
        return redirect(url_for('seller.office'))
    return render_template("officePage.html", subscribe=subscribe)

@seller.route("/contact_us", strict_slashes=False, methods=["GET", "POST"])
def contact_us():
    """_summary_

	Returns:
		_type_: _description_
	"""
    subscribe = SubscribeForm()
    contact = ContactForm()
    if contact.validate_on_submit() and request.method == "POST":
        content = {"firstname": contact.firstname.data,
                   "lastname": contact.lastname.data,
                   "email": contact.email.data,
                   "topic": contact.topic.data,
                   "description": contact.description.data}
        contact_us_mail(content=content)
        flash("Submitted Successfully")
        return redirect(url_for('seller.contact_us'))
    if subscribe.validate_on_submit() and request.method == 'POST':
        subscribe_mail([subscribe.email.data])
        return redirect(url_for('seller.contact_us'))
    return render_template("contactPage.html", subscribe=subscribe, contact=contact)


@seller.route("/seller_guide", strict_slashes=False, methods=["GET", "POST"])
def seller_guide():
    """_summary_

	Returns:
		_type_: _description_
	"""
    subscribe = SubscribeForm()
    if subscribe.validate_on_submit() and request.method == 'POST':
        subscribe_mail([subscribe.email.data])
        return redirect(url_for('seller.seller_guide'))
    return render_template("guidePage.html", subscribe=subscribe)
