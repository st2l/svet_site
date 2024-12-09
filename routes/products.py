from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory
from models import db, User

def products():
    page = request.args.get('page', 1, type=int)
    per_page = 4 * 5  # Number of items per page

    lamps_pagination = Lamp.query.paginate(page=page, per_page=per_page, error_out=False)
    lamps = lamps_pagination.items
    categories = Category.query.all()
    subcategories = SubCategory.query.all()
    sub_subcategories = SubSubCategory.query.all()

    params = {
        'lamps': lamps,
        'categories': categories,
        'subcategories_names': [el.name for el in subcategories],
        'subcategories': subcategories,
        'sub_subcategories': sub_subcategories,
        'pagination': lamps_pagination
    }

    return render_template('products.html', **params)