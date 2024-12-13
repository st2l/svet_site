from flask import request, render_template
from models import Lamp
from helpers import filter_params


def search(search_option=None, search_text=None):
    """
    Handle search requests for lamps based on different search options.
    This function processes both POST and GET requests to search for lamps
    in the database. It supports searching by name, description, or article.
    The results are paginated and rendered in the 'search.html' template.
    
    Args:
        search_option (str, optional): The field to search by ('name', 'description', or 'article'). Defaults to None.
        search_text (str, optional): The text to search for in the specified field. Defaults to None.
    Returns:
        Response: The rendered 'search.html' template with search results and pagination.
    """
    

    if request.method == 'POST':  # of it's form so we need to get data from form

        search_option = request.form.get('search_option', 'wtf')
        search_text = request.form.get('search', 'wtf')

    else:

        search_option = request.args.get('search_option', 'wtf')
        search_text = request.args.get('search_text', 'wtf')

    print(search_option, search_text)

    if search_option == 'name':
        lamps = Lamp.query.filter(Lamp.name.like(f'%{search_text}%'))
    elif search_option == 'description':
        lamps = Lamp.query.filter(
            Lamp.description.like(f'%{search_text}%'))
    else:
        lamps = Lamp.query.filter(
            Lamp.article.like(f'%{search_text}%'))

    # pagination for lamps
    page = request.args.get('page', 1, type=int)
    lamps_paginator = lamps.paginate(
        page=page, per_page=4 * 5, error_out=False)
    lamps = lamps_paginator.items

    params = {
        'lamps': lamps,
        'pagination': lamps_paginator,
        'search_option': search_option,
        'search_text': search_text
    }

    params.update(filter_params())

    return render_template('search.html', **params)
