"""
"""

from api.utils.flaskforms import SellerSearchForm, SubscribeForm, AddProductForm
from api.models import Product
from api.models import Review
from api.models import Purchase

from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from cloudinary.uploader import upload

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

    if form.validate_on_submit() and request.method == "POST":
        return render_template("homePage.html",
                               form=form,
                               subscribe=subscribe,
                               user=current_user
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
        image_file = upload_result["secure_url"]

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
                               user=current_user)

    return render_template("addProduct.html",
                           form=form,
                           subscribe=subscribe,
                           user=current_user
                           )


@seller.route("/<link>", strict_slashes=False, methods=['GET', 'POST', 'DELETE', 'PUT'])
@login_required
def product(link):
    """_summary_

	Args:
		name (str): _description_
	"""

    product = Product.query.filter_by(link=link).first()
    review = Review.query.filter_by(product_id=product.id).all()
    purchase = Purchase.query.filter_by(product_id=product.id).all()

    # forms
    form = AddProductForm(obj=product)
    subscribe = SubscribeForm()

    return render_template("productPage.html",
                           form=form,
                           subscribe=subscribe,
                           product=product,
                           review=review,
                           purchase=purchase,
                           user=current_user)
