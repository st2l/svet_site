from flask import render_template, request, redirect, url_for, flash
from models import db, User


def index():
    return render_template('index.html')
