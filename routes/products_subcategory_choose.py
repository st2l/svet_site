from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory, CartItem
from flask_login import current_user
from models import db, User
from helpers import filter_params


def products_subcategory_choose(category_id, subcategory_id):
    """
    Обрабатывает выбор подкатегории продуктов и отображает соответствующие товары.
    Аргументы:
        category_id (int): Идентификатор категории.
        subcategory_id (int): Идентификатор подкатегории.
    """

    page = request.args.get('page', 1, type=int)
    per_page = 4 * 5  # Number of items per page

    what_Ssubs_good = [
        el.id for el in SubSubCategory.query.filter(
            SubSubCategory.subcategory_id == subcategory_id
        ).all()
    ]

    lamps_pagination = Lamp.query.filter(
        Lamp.subsubcategory_id.in_(
            what_Ssubs_good
        )
    ).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    lamps = lamps_pagination.items

    params = {
        'lamps': lamps,
        'chosen_subcat': subcategory_id,
        'pagination': lamps_pagination,
        'chosen_cat': category_id,
    }

    params.update(filter_params())

    return render_template('products_subcategory.html', **params)
