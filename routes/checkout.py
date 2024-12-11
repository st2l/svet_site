from flask import render_template, redirect, url_for, request
from flask_login import current_user
from models import db, User, CartItem, Lamp, Category, SubCategory, SubSubCategory
from helpers import filter_params


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

    # proceed the default categories
    params = filter_params()

    return render_template('checkout.html', **params)