from flask import render_template, request, redirect, url_for, flash
from models import db, User
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user


def logout():
    """
    Завершает сеанс пользователя и перенаправляет на главную страницу.

    Возвращает:
        Response: Перенаправление на главную страницу.
    """
    logout_user()
    return redirect('/')
