from .index import index
from .login import login
from .register import register
from .products import products
from .contact import contact
from .logout import logout

from flask import Flask


def register_all_routes(app: Flask):

    app.add_url_rule(rule='/', view_func=index, methods=['GET'])

    app.add_url_rule(rule='/login', view_func=login, methods=['GET', 'POST'])

    app.add_url_rule(rule='/register', view_func=register,
                     methods=['GET', 'POST'])

    app.add_url_rule(rule='/products', view_func=products, methods=['GET'])

    app.add_url_rule(rule='/contact', view_func=contact, methods=['GET'])

    app.add_url_rule(rule='/logout', view_func=logout, methods=['GET', 'POST'])
