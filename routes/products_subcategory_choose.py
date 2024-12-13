from flask import render_template, request, redirect, url_for, flash
from models import Lamp, Category, SubCategory, SubSubCategory, CartItem
from flask_login import current_user
from models import db, User
from helpers import filter_params


def products_subcategory_choose(category_id, subcategory_id):
    """
    Handles the selection of products based on the given category and subcategory IDs.
    
    Args:
        category_id (int): The ID of the category.
        subcategory_id (int): The ID of the subcategory.
    Returns:
        str: The rendered HTML template for the products subcategory page.
    
    This function performs the following steps:
    1. Retrieves the current page number from the request arguments, defaulting to 1.
    2. Sets the number of items per page.
    3. Queries the database for sub-subcategories that belong to the given subcategory.
    4. Queries the database for lamps that belong to the retrieved sub-subcategories.
    5. Paginates the lamp results.
    6. Prepares the parameters for rendering the template, including lamps, chosen subcategory, pagination, and chosen category.
    7. Updates the parameters with additional filter parameters.
    8. Renders and returns the 'products_subcategory.html' template with the prepared parameters.
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
