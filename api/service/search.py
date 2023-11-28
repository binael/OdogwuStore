from api.models import Product
from collections import OrderedDict

def search_product(id=None, category=None, product=None, filter={}):
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
    if category and category != "none" and category != "":
        query = query.filter_by(category=category)
    result = query
    sub_result = query

    if product and product.strip() != "":
        product_list = product.split(" ")
        # [AND SEARCH] in Product name and sub_category
        for item in product_list:
            result = result.filter(Product.name.like(f"%{item}%"))
            sub_result = sub_result.filter(Product.sub_category.like(f"%{item}%"))

        result = result.all()
        result.extend(sub_result.all())

        # [OR SEARCH] in Product name and sub_category
        if len(product_list) > 1:
            product_set = set(product_list)
            for item in product_set:
                new_sub = query.filter(Product.name.like(f"%{item}%")).all()
                new_result = query.filter(Product.name.like(f"%{item}%")).all()
                result.extend(new_result)
                result.extend(new_sub)

    return list(OrderedDict.fromkeys(result))

def buyer_search(product, filter):
    pass
