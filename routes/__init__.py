from .index import index
from .login import login
from .register import register
from .products import products
from .contact import contact
from .logout import logout
from .products_full_choose import products_full_choose
from .products_category_choose import products_category_choose
from .products_subcategory_choose import products_subcategory_choose
from .lamps import get_lamp
from .add_to_cart import add_to_cart
from .cart import view_cart, increase_item,  decrease_item, delete_item
from .checkout import checkout
from .search import search

from helpers import filter_params

from flask import Flask
from flask_login import login_required


def register_all_routes(app: Flask):

    app.add_url_rule(rule='/', view_func=index, methods=['GET'])

    app.add_url_rule(rule='/login', view_func=login, methods=['GET', 'POST'])

    app.add_url_rule(rule='/register', view_func=register,
                     methods=['GET', 'POST'])

    app.add_url_rule(rule='/products', view_func=products, methods=['GET'])

    app.add_url_rule(rule='/contact', view_func=contact, methods=['GET'])

    app.add_url_rule(rule='/logout', view_func=logout, methods=['GET', 'POST'])

    app.add_url_rule(
        rule='/products/<int:category_id>',
        view_func=products_category_choose,
        methods=['GET']
    )

    app.add_url_rule(
        rule='/products/<int:category_id>/<int:subcategory_id>',
        view_func=products_subcategory_choose,
        methods=['GET']
    )

    app.add_url_rule(
        rule='/products/<int:category_id>/<int:subcategory_id>/<int:sub_subcategory_id>',
        view_func=products_full_choose,
        methods=['GET']
    )

    app.add_url_rule(
        rule='/lamp/<int:lamp_id>',
        view_func=get_lamp,
        methods=['GET']
    )

    app.add_url_rule(
        rule='/add_to_cart/<int:lamp_id>',
        view_func=add_to_cart,
        methods=['GET']
    )

    app.add_url_rule(
        rule='/cart',
        view_func=view_cart,
        methods=['GET']
    )

    @app.route('/cart/increase/<int:item_id>', methods=['GET', 'POST'])
    def increase_item_route(item_id):
        return increase_item(item_id)

    @app.route('/cart/decrease/<int:item_id>', methods=['GET', 'POST'])
    def decrease_item_route(item_id):
        return decrease_item(item_id)

    @app.route('/cart/delete/<int:item_id>', methods=['GET', 'POST'])
    def delete_item_route(item_id):
        return delete_item(item_id)

    @login_required
    @app.route('/checkout', methods=['GET', 'POST'])
    def checkout_route():
        return checkout()

    @app.route('/search', methods=['GET', 'POST'])
    def search_route():
        return search()
