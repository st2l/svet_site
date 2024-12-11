from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory, CartItem
from models import db, User
from flask_login import current_user
from helpers import filter_params


def products_full_choose(category_id, subcategory_id, sub_subcategory_id):
    page = request.args.get('page', 1, type=int)
    per_page = 4 * 5  # Number of items per page

    # lamps need to be sorted carefully (not really)
    lamps_pagination = Lamp.query.filter_by(subsubcategory_id=sub_subcategory_id).paginate(
        page=page, per_page=per_page, error_out=False)
    lamps = lamps_pagination.items

    params = {
        'pagination': lamps_pagination,
        'chosen_cat': category_id,
        'chosen_subcat': subcategory_id,
        'chosen_sub_subcat': sub_subcategory_id,
        'lamps': lamps,
    }

    params.update(filter_params())

    return render_template('products_full.html', **params)
