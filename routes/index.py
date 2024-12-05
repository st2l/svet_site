from flask import render_template, request, redirect, url_for, flash
from models import db, User, Lamp
from random import randint


def index():

    lamps = Lamp.query.all()
    if lamps:
        params = {
            'lamps': lamps[:3]
        }
    else:
        params = {
            'lamps': []
        }

    return render_template('index.html', **params)
