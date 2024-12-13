from flask import render_template, redirect, url_for, request
from flask_login import current_user
from models import db, User, CartItem, Lamp
from helpers import filter_params


def view_cart():
    """
    Handle the view cart request.
    This function checks if the current user is authenticated. If not, it returns a 401 status code with a message indicating that the user is not logged in. If the user is authenticated, it filters the parameters and renders the 'cart.html' template with the filtered parameters.

    Returns:
        tuple: A message and a status code if the user is not authenticated.
        str: Rendered 'cart.html' template with filtered parameters if the user is authenticated.
    """

    if not current_user.is_authenticated:
        return "User not logged in", 401

    params = filter_params()
    return render_template('cart.html', **params)


def increase_item(item_id):
    if not current_user.is_authenticated:
        return "User not logged in", 401

    cart_item = CartItem.query.get(item_id)
    if cart_item and cart_item.user_id == current_user.id:
        cart_item.amount += 1
        db.session.commit()

    return redirect('/cart')


def decrease_item(item_id):
    if not current_user.is_authenticated:
        return "User not logged in", 401

    cart_item = CartItem.query.get(item_id)
    if cart_item and cart_item.user_id == current_user.id:
        if cart_item.amount > 1:
            cart_item.amount -= 1
        else:
            db.session.delete(cart_item)
        db.session.commit()

    return redirect('/cart')


def delete_item(item_id):
    if not current_user.is_authenticated:
        return "User not logged in", 401

    cart_item = CartItem.query.get(item_id)
    if cart_item and cart_item.user_id == current_user.id:
        db.session.delete(cart_item)
        db.session.commit()

    return redirect('/cart')
