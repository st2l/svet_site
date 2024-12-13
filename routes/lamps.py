from flask import jsonify, request
from flask import render_template
from models import Lamp, Category, SubCategory, SubSubCategory
from flask_login import current_user
from helpers import filter_params


def get_lamp(lamp_id):
    """
    Retrieve and render a lamp by its ID.
    
    Args:
        lamp_id (int): The ID of the lamp to retrieve.
    Returns:
        tuple: A tuple containing the rendered template and HTTP status code.
            - If the lamp is found, returns a rendered 'lamp.html' template with lamp details and a 200 status code.
            - If the lamp is not found, returns a JSON response with an error message and a 404 status code.
    """

    lamp = Lamp.query.filter_by(id=lamp_id).first()

    params = {
        'lamp': lamp,
        'enumerate': enumerate,
        'len': len,
        'extra_images': [lamp.main_image, lamp.photo1, lamp.photo2, lamp.photo3, lamp.photo4, lamp.photo5, lamp.photo6, lamp.photo7, lamp.photo8, lamp.photo9, lamp.photo10, lamp.photo11, lamp.photo12, lamp.photo13, lamp.photo14, lamp.photo15, lamp.photo16, lamp.photo17, lamp.photo18, lamp.photo19, lamp.photo20],
    }

    params.update(filter_params())

    if lamp:
        return render_template('lamp.html', **params), 200
    else:
        return jsonify({"error": "Lamp not found"}), 404
