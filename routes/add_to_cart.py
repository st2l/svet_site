from flask import request, redirect, url_for, jsonify
from models import db, CartItem
from flask_login import current_user


def add_to_cart(lamp_id):
    """
    Add a lamp to the shopping cart.
    This function handles the addition of a lamp to the user's shopping cart. 
    It performs the following steps:
    1. Validates the provided lamp ID.
    2. Checks if the user is authenticated.
    3. Checks if the lamp is already in the user's cart.
    4. If the lamp is already in the cart, redirects to increase the quantity.
    5. If the lamp is not in the cart, adds it to the cart and commits the change to the database.

    Args:
        lamp_id (int): The ID of the lamp to be added to the cart.
    Returns:
        Response: A redirect to the appropriate URL based on the operation performed.
    """

    if not lamp_id:
        return jsonify({'error': 'Invalid product ID', 'status': 'error'}), 200

    if not current_user.is_authenticated:
        return jsonify({'error': 'User is not authenticated', 'status': 'error'}), 200

    existed_crt_item = CartItem.query.filter_by(
        user_id=current_user.id, lamp_id=lamp_id).first()

    if existed_crt_item:
        return redirect(f'/cart/increase/{existed_crt_item.id}')

    cart_item = CartItem(user_id=current_user.id, lamp_id=lamp_id)
    db.session.add(cart_item)
    db.session.commit()

    return jsonify({'status': 'success'}), 200
