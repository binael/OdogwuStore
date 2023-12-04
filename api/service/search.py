from api.models import Product
from collections import OrderedDict

CATEGORY = {
    "appliances": "Appliances",
    "computer-accessories": "Computer and Accessories",
    "fashion": "Fashion",
    "furniture": "Furniture",
    "games-toys": "Games and Toys",
    "groceries": "Groceries",
    "health-beauty": "Health and Beauty",
    "home-office": "Home and Office",
    "jewelries-watches": "Jewelries and Watches",
    "phones-tablets": "Phones and Tablets",
    "other-categories": "Other Categories"
}

def search_product(id=None, category=None, product=None, filter=None):
    """_summary_

	Args:
		id (_type_, optional): _description_. Defaults to None.
		category (_type_, optional): _description_. Defaults to None.
		product (_type_, optional): _description_. Defaults to None.
		filter (dict, optional): _description_. Defaults to {}.

	Returns:
		_type_: _description_
	"""
    if id:
        return seller_search(id, category, product)
    return buyer_search(product, filter)

def seller_search(id, category, product):
    query = Product.query.filter_by(seller_id=id)
    # Ensure category search
    if category and category != "none":
        query = query.filter_by(category=category)
    result = query
    sub_result = query
    cat = query

    if product and product.strip() != "":
        product_list = product.split(" ")
        # [AND SEARCH] in Product name and sub_category
        for item in product_list:
            result = result.filter(Product.name.like(f"%{item}%"))
            sub_result = sub_result.filter(Product.sub_category.like(f"%{item}%"))
            if not category or category == "none":
                cat = cat.filter(Product.category.like(f"%{item}%"))
        result = result.all()
        result.extend(sub_result.all())
        if not category or category == "none":
            result.extend(cat.all())

        # [OR SEARCH] in Product name and sub_category and category
        if len(product_list) > 1:
            product_set = set(product_list)
            for item in product_set:
                new_sub = query.filter(Product.name.like(f"%{item}%")).all()
                new_result = query.filter(Product.sub_category.like(f"%{item}%")).all()
                result.extend(new_result)
                result.extend(new_sub)
                if not category or category == "none":
                    new_cat = query.filter(Product.category.like(f"%{item}%")).all()
                    result.extend(new_cat)

    return list(OrderedDict.fromkeys(result))

def buyer_search(product, filter):
    pass


def search_a_product(name):
    if name in CATEGORY:
        return Product.query.filter_by(category=CATEGORY.get(name).lower()).all()
    else:
        return Product.query.filter_by(link=name).first()
