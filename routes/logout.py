from flask import render_template, request, redirect, url_for, flash
from models import db, User
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user


def logout():
    logout_user()
    return redirect('/')
