from flask import request, jsonify, url_for
from models import db, CartItem
from flask_login import current_user

def add_to_cart():
    data = request.get_json()
    lamp_id = data.get('productId')

    if not lamp_id:
        return jsonify({'error': 'Invalid product ID'}), 400

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    cart_item = CartItem(user_id=current_user.id, lamp_id=lamp_id)
    db.session.add(cart_item)
    db.session.commit()

    return jsonify({'message': 'Товар добавлен в корзину!'}), 200
