from functools import wraps
from flask import request
from flask_login import current_user
from models import Category, SubCategory, SubSubCategory, CartItem, Lamp


def filter_params():
    """
    Фильтрует параметры для категорий и корзины.
    Возвращает словарь с параметрами, включающими категории, подкатегории, 
    под-подкатегории, элементы корзины и информацию о текущем пользователе.
    Возвращаемое значение:
        dict: Словарь с параметрами:
            - categories (list): Список всех категорий.
            - subcategories_names (list): Список имен всех подкатегорий.
            - subcategories (list): Список всех подкатегорий.
            - sub_subcategories (list): Список всех под-подкатегорий.
            - cart_items (list): Список элементов корзины текущего пользователя.
            - current_user (User): Текущий пользователь.
            - len_cart_items (int): Количество элементов в корзине.
            - full_price (float): Общая стоимость всех элементов в корзине.
    """
    

    params = {}

    # get all categories and subcategories and sub_subcategories
    categories = Category.query.all()
    subcategories = SubCategory.query.all()
    sub_subcategories = SubSubCategory.query.all()

    # try for getting all from cart (if user is logged in)
    if current_user.is_authenticated:
        try:
            cart_items = CartItem.query.filter_by(
                user_id=current_user.id).all()
            cart_lamp_ids = [item.lamp_id for item in cart_items]
            cart_lamps = Lamp.query.filter(
                Lamp.id.in_(cart_lamp_ids)).all()

            for item in cart_items:
                item.lamp = next(
                    (lamp for lamp in cart_lamps if lamp.id == item.lamp_id), None)
        except:
            cart_items = []
            cart_lamps = []
    else:  # if there is no user logged in
        cart_items = []
        cart_lamps = []

    # update the params
    params['categories'] = categories
    params['subcategories_names'] = [el.name for el in subcategories]
    params['subcategories'] = subcategories
    params['sub_subcategories'] = sub_subcategories
    params['cart_items'] = cart_items
    params['current_user'] = current_user
    params['len_cart_items'] = cart_items.__len__()
    params['full_price'] = sum(
        item.amount * item.lamp.price for item in cart_items)

    return params
