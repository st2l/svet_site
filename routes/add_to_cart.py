from flask import request, redirect, url_for
from models import db, CartItem
from flask_login import current_user

def add_to_cart(lamp_id):
    """
    Добавляет товар в корзину.
    Аргументы:
        lamp_id (int): Идентификатор товара (лампы), который нужно добавить в корзину.
    Возвращает:
        Response: Перенаправляет на страницу корзины с обновленным товаром или страницу входа, если пользователь не аутентифицирован.
    """

    if not lamp_id:
        return jsonify({'error': 'Invalid product ID'}), 400

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    existed_crt_item = CartItem.query.filter_by(
        user_id=current_user.id, lamp_id=lamp_id).first()
    
    if existed_crt_item:
        return redirect(f'/cart/increase/{existed_crt_item.id}')

    cart_item = CartItem(user_id=current_user.id, lamp_id=lamp_id)
    db.session.add(cart_item)
    db.session.commit()

    return redirect(url_for('view_cart'))
