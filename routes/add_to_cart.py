from flask import request, redirect, url_for
from models import db, CartItem
from flask_login import current_user

def add_to_cart(lamp_id):

    if not lamp_id:
        return jsonify({'error': 'Invalid product ID'}), 400

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    cart_item = CartItem(user_id=current_user.id, lamp_id=lamp_id)
    db.session.add(cart_item)
    db.session.commit()

    return redirect(url_for('view_cart'))
