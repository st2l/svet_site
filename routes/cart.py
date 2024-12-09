from flask import render_template, redirect, url_for, request
from flask_login import current_user
from models import db, User, CartItem, Lamp

def view_cart():
    if not current_user.is_authenticated:
        return "User not logged in", 401

    user = User.query.get(current_user.id)
    if not user:
        return "User not found", 404

    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    lamp_ids = [item.lamp_id for item in cart_items]
    lamps = Lamp.query.filter(Lamp.id.in_(lamp_ids)).all()

    for item in cart_items:
        item.lamp = next((lamp for lamp in lamps if lamp.id == item.lamp_id), None)

    return render_template('cart.html', user=user, cart_items=cart_items)

def increase_item(item_id):
    if not current_user.is_authenticated:
        return "User not logged in", 401

    cart_item = CartItem.query.get(item_id)
    if cart_item and cart_item.user_id == current_user.id:
        cart_item.amount += 1
        db.session.commit()

    return redirect(url_for('view_cart'))

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

    return redirect(url_for('view_cart'))

def delete_item(item_id):
    if not current_user.is_authenticated:
        return "User not logged in", 401

    cart_item = CartItem.query.get(item_id)
    if cart_item and cart_item.user_id == current_user.id:
        db.session.delete(cart_item)
        db.session.commit()

    return redirect(url_for('view_cart'))