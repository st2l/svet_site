from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory, CartItem
from models import db, User
from flask_login import current_user


def products():
    page = request.args.get('page', 1, type=int)
    per_page = 4 * 5  # Number of items per page

    lamps_pagination = Lamp.query.paginate(
        page=page, per_page=per_page, error_out=False)
    lamps = lamps_pagination.items
    categories = Category.query.all()
    subcategories = SubCategory.query.all()
    sub_subcategories = SubSubCategory.query.all()

    try:
        cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
        cart_lamp_ids = [item.lamp_id for item in cart_items]
        cart_lamps = Lamp.query.filter(Lamp.id.in_(cart_lamp_ids)).all()

        for item in cart_items:
            item.lamp = next(
                (lamp for lamp in cart_lamps if lamp.id == item.lamp_id), None)
    except:
        cart_items = []
        cart_lamps = []

    params = {
        'lamps': lamps,
        'categories': categories,
        'subcategories_names': [el.name for el in subcategories],
        'subcategories': subcategories,
        'sub_subcategories': sub_subcategories,
        'pagination': lamps_pagination,
        'cart_items': cart_items,
        'current_user': current_user,
        'len_cart_items': cart_items.__len__(),
        'sum_of_cart_items': sum([item.amount * item.lamp.price for item in cart_items]),

    }

    return render_template('products.html', **params)
