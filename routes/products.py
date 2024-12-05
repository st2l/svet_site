from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory
from models import db, User


def products():
    
    lamps = Lamp.query.all()
    categories = Category.query.all()
    subcategories = SubCategory.query.all()
    sub_subcategories = SubSubCategory.query.all()
    if lamps:
        params = {
            'lamps': lamps[:3]
        }
    else:
        params = {
            'lamps': []
        }
    params['categories'] = categories
    params['subcategories'] = subcategories
    params['sub_subcategories'] = sub_subcategories

    return render_template('products.html', **params)
