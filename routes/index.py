from flask import render_template
from helpers import filter_params
from models import Category, Lamp


def index():
    """
    Renders the index page with specific parameters.
    This function queries the database to retrieve the category ID for "Парковые фонари"
    and the 15 most expensive lamps. It then combines these parameters with additional
    filter parameters and renders the 'index.html' template with the combined parameters.
    
    Returns:
        str: The rendered HTML content for the index page.
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
