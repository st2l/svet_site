from flask import request, render_template
from models import Lamp
from helpers import filter_params


def search(search_option=None, search_text=None):

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
