from flask import render_template
from helpers import filter_params


def index():
    return render_template('index.html', **filter_params())
