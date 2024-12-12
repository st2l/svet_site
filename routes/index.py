from flask import render_template
from helpers import filter_params
from models import Category, Lamp


def index():
    park_lights_idx = Category.query.filter(Category.name.contains("Парковые фонари")).first()
    expensive_lamps = Lamp.query.order_by(Lamp.price.desc()).limit(15).all()

    params = {
        'park_lights_idx': park_lights_idx.id,
        'lamps': expensive_lamps,
        
    }

    params.update(filter_params())

    return render_template('index.html', **params)
