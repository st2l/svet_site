from flask import render_template
from helpers import filter_params
from models import Category, Lamp


def index():
    """
    Главная страница сайта.
    Возвращает главную страницу сайта с параметрами, включающими идентификатор категории "Парковые фонари" 
    и список самых дорогих ламп.
    Возвращаемые параметры:
        park_lights_idx (int): Идентификатор категории "Парковые фонари".
        lamps (list): Список объектов Lamp, отсортированных по убыванию цены, ограниченный 15 элементами.
        **params: Дополнительные параметры, возвращаемые функцией filter_params().
    Возвращает:
        str: Сгенерированный HTML-код главной страницы.
    """

    park_lights_idx = Category.query.filter(
        Category.name.contains("Парковые фонари")).first()
    expensive_lamps = Lamp.query.order_by(Lamp.price.desc()).limit(15).all()

    params = {
        'park_lights_idx': park_lights_idx.id,
        'lamps': expensive_lamps,
    }

    params.update(filter_params())

    return render_template('index.html', **params)
