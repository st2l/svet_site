from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory
from models import db, User

def products_full_choose(category_id, subcategory_id, sub_subcategory_id):
    page = request.args.get('page', 1, type=int)
    per_page = 4 * 5  # Number of items per page

    # don't change categories for the aside panel
    categories = Category.query.all()
    subcategories = SubCategory.query.all()
    sub_subcategories = SubSubCategory.query.all()

    # lamps need to be sorted carefully (not really)
    lamps_pagination = Lamp.query.filter_by(subsubcategory_id=sub_subcategory_id).paginate(page=page, per_page=per_page, error_out=False)
    lamps = lamps_pagination.items

    params = {
        'lamps': lamps,
        'categories': categories,
        'subcategories_names': [el.name for el in subcategories],
        'subcategories': subcategories,
        'sub_subcategories': sub_subcategories,
        'pagination': lamps_pagination,
        'chosen_cat': category_id,
        'chosen_subcat': subcategory_id,
        'chosen_sub_subcat': sub_subcategory_id,
    }

    return render_template('products_full.html', **params)