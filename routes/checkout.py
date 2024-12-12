from flask import render_template, redirect, url_for, request
from flask_login import current_user
from models import db, User, CartItem, Lamp, Category, SubCategory, SubSubCategory
from helpers import filter_params
from conf import Config
from helpers import send_email


def checkout():

    if request.method == 'POST':  # if the form is submitted
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        payment_method = request.form.get('payment_method')

        message = f"""От клиента:
        - email: {current_user.email}
        - имя: {first_name}
        - фамилия: {last_name}
        - телефон: {phone_number}
        - адрес: {address}
        - способ оплаты, который выбрал пользователь: {payment_method}
        Поступило заявление на согласование заказа. Заказ включает в себя следующие товары:"""

        users_cart_items = CartItem.query.filter_by(
            user_id=current_user.id).all()

        for item in users_cart_items:
            lamp = Lamp.query.get(item.lamp_id)
            message += f"\n- {lamp.name} ({lamp.price} руб./шт.) Артикул: {lamp.article}, Количество: {item.amount}. Сумма: {lamp.price * item.amount} руб."

        message += f'\n-----------\nОбщая сумма заказа: {sum([item.amount * Lamp.query.get(item.lamp_id).price for item in users_cart_items])} руб.'

        # Example usage
        send_email(
            Config.MANAGER_EMAIL,
            'Поступило согласование заказа!',
            message
        )

        # clear all cartItems from user
        CartItem.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        
        return redirect('/') 

    if not current_user.is_authenticated:
        return "User not logged in", 401

    user = User.query.get(current_user.id)
    if not user:
        return "User not found", 404

    # proceed the default categories
    params = filter_params()

    return render_template('checkout.html', **params)
