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
        'sub_subcategories': sub_subcategories
    }

    if lamp:
        return render_template('lamp.html', **params), 200
    else:
        return jsonify({"error": "Lamp not found"}), 404
