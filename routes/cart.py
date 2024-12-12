from flask import render_template, redirect, url_for, request
from flask_login import current_user
from models import db, User, CartItem, Lamp
from helpers import filter_params


def view_cart():
    """
    Отображает содержимое корзины пользователя.
    Если пользователь не аутентифицирован, возвращает сообщение об ошибке и статус 401.
    В противном случае фильтрует параметры и отображает шаблон 'cart.html' с этими параметрами.
    Возвращает:
        str: Сообщение об ошибке, если пользователь не аутентифицирован.
        int: Статус код 401, если пользователь не аутентифицирован.
        str: Отрендеренный шаблон 'cart.html' с параметрами.
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
