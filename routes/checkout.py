from flask import render_template, redirect, url_for, request
from flask_login import current_user
from models import db, User, CartItem, Lamp, Category, SubCategory, SubSubCategory

def checkout():

    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        payment_method = request.form.get('payment_method')

        # TODO: write function for email sending

        print(first_name, last_name, phone_number, address, payment_method)

    if not current_user.is_authenticated:
        return "User not logged in", 401

    user = User.query.get(current_user.id)
    if not user:
        return "User not found", 404

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
        'categories': categories,
        'subcategories_names': [el.name for el in subcategories],
        'subcategories': subcategories,
        'sub_subcategories': sub_subcategories,
        'cart_items': cart_items,
        'current_user': current_user,
        'len_cart_items': cart_items.__len__(),
        'sum_of_cart_items': sum([item.amount * item.lamp.price for item in cart_items]),
        'full_price': sum(item.amount * item.lamp.price for item in cart_items),

    }

    return render_template('checkout.html', **params)