from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory, CartItem
from flask_login import current_user
from models import db, User
from helpers import filter_params


def products_category_choose(category_id):
    """
    Обрабатывает выбор категории продуктов и отображает соответствующие лампы на странице.
    Аргументы:
        category_id (int): Идентификатор выбранной категории.
    Описание:
        Функция получает номер страницы из параметров запроса и определяет количество элементов на странице.
        Затем она находит все подкатегории и под-подкатегории, связанные с выбранной категорией.
        После этого функция выполняет пагинацию ламп, принадлежащих найденным под-подкатегориям.
        В конце функция рендерит HTML-шаблон 'products_category.html' с параметрами, включающими список ламп,
        объект пагинации и идентификатор выбранной категории.
    """

    page = request.args.get('page', 1, type=int)
    per_page = 4 * 5  # Number of items per page

    what_subs_good = [
        el.id for el in
        SubCategory.query.filter_by(
            category_id=category_id
        ).all()
    ]

    what_Ssubs_good = [
        el.id for el in
        SubSubCategory.query.filter(
            SubSubCategory.subcategory_id.in_(what_subs_good)
        ).all()
    ]

    lamps_pagination = Lamp.query.filter(
        Lamp.subsubcategory_id.in_(what_Ssubs_good)
    ).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    lamps = lamps_pagination.items

    params = {
        'lamps': lamps,
        'pagination': lamps_pagination,
        'chosen_cat': category_id,
    }

    params.update(filter_params())

    return render_template('products_category.html', **params)
