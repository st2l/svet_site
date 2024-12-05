from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory
from models import db, User


def products_subcategory_choose(category_id, subcategory_id):

    # don't change categories for the aside panel
    categories = Category.query.all()
    subcategories = SubCategory.query.all()
    sub_subcategories = SubSubCategory.query.all()

    what_Ssubs_good = [el.id for el in SubSubCategory.query.filter(SubSubCategory.subcategory_id == subcategory_id).all()]
    lamps = Lamp.query.filter(Lamp.subsubcategory_id.in_(what_Ssubs_good)).all()

    params = {
        'lamps': lamps,
        'categories': categories,
        'subcategories': subcategories,
        'sub_subcategories': sub_subcategories,
    }

    return render_template('products.html', **params)
