from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory, CartItem
from models import db, User
from flask_login import current_user
from helpers import filter_params


def products():
    page = request.args.get('page', 1, type=int)
    per_page = 4 * 5  # Number of items per page

    lamps_pagination = Lamp.query.paginate(
        page=page, per_page=per_page, error_out=False)
    lamps = lamps_pagination.items

    params = {
        'lamps': lamps,
        'pagination': lamps_pagination,
    }

    params.update(filter_params())

    return render_template('products.html', **params)
