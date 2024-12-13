from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory, CartItem
from models import db, User
from flask_login import current_user
from helpers import filter_params


def products():
    """
    Обрабатывает запрос на получение списка продуктов и возвращает отрендеренный HTML шаблон.
    Запросы:
        page (int, optional): Номер страницы для пагинации. По умолчанию 1.
    Возвращает:
        str: Отрендеренный HTML шаблон с продуктами и параметрами пагинации.
    """
    

    page = request.args.get('page', 1, type=int)
    per_page = 4 * 5  # Number of items per page

    lamps_pagination = Lamp.query.paginate(
        page=page, per_page=per_page, error_out=False)
    lamps = lamps_pagination.items

    params = {
        'lamps': lamps,
        'pagination': lamps_pagination,
    }

    params.update(filter_params())

    return render_template('products.html', **params)
