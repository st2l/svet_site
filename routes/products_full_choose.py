from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory
from models import db, User


def products_full_choose(category_id, subcategory_id, sub_subcategory_id):

    # don't change categories for the aside panel
    categories = Category.query.all()
    subcategories = SubCategory.query.all()
    sub_subcategories = SubSubCategory.query.all()

    # lamps need to be sorted carefully (not really)
    lamps = Lamp.query.filter_by(subsubcategory_id=sub_subcategory_id)

    params = {
        'lamps': lamps,
        'categories': categories,
        'subcategories_names': [el.name for el in subcategories],
        'subcategories': subcategories,
        'sub_subcategories': sub_subcategories,
    }

    return render_template('products.html', **params)
