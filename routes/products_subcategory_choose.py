from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory
from models import db, User


def products_subcategory_choose(category_id, subcategory_id):
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Number of items per page

    # don't change categories for the aside panel
    categories = Category.query.all()
    subcategories = SubCategory.query.all()
    sub_subcategories = SubSubCategory.query.all()

    what_Ssubs_good = [el.id for el in SubSubCategory.query.filter(
        SubSubCategory.subcategory_id == subcategory_id).all()]
    lamps_pagination = Lamp.query.filter(Lamp.subsubcategory_id.in_(
        what_Ssubs_good)).paginate(page=page, per_page=per_page, error_out=False)
    lamps = lamps_pagination.items

    params = {
        'lamps': lamps,
        'categories': categories,
        'subcategories_names': [el.name for el in subcategories],
        'subcategories': subcategories,
        'sub_subcategories': sub_subcategories,
        'pagination': lamps_pagination
    }

    return render_template('products.html', **params)
