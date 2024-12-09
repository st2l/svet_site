from flask import jsonify, request
from flask import render_template
from models import Lamp, Category, SubCategory, SubSubCategory


def get_lamp(lamp_id):
    lamp = Lamp.query.filter_by(id=lamp_id).first()

    categories = Category.query.all()
    subcategories = SubCategory.query.all()
    sub_subcategories = SubSubCategory.query.all()

    params = {
        'lamp': lamp,
        'categories': categories,
        'subcategories_names': [el.name for el in subcategories],
        'subcategories': subcategories,
        'sub_subcategories': sub_subcategories,
        'enumerate': enumerate,
        'extra_images': [el for el in [lamp.photo1, lamp.photo2, lamp.photo3, lamp.photo4, lamp.photo5, lamp.photo6, lamp.photo7, lamp.photo8, lamp.photo9, lamp.photo10, lamp.photo11, lamp.photo12, lamp.photo13, lamp.photo14, lamp.photo15, lamp.photo16, lamp.photo17, lamp.photo18, lamp.photo19, lamp.photo20] if el not in [None, '']]
    }

    if lamp:
        return render_template('lamp.html', **params), 200
    else:
        return jsonify({"error": "Lamp not found"}), 404
