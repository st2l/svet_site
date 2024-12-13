from flask import render_template, request, redirect, url_for, flash
from models import db, User
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from helpers import filter_params


def login():
    """
    Обрабатывает запросы на вход пользователя.
    POST:
        Получает email и пароль из формы запроса.
        Проверяет наличие пользователя с данным email.
        Если пользователь существует, проверяет правильность пароля.
        При успешной проверке пароля, выполняет вход пользователя и перенаправляет на главную страницу.
        В случае неправильного пароля возвращает сообщение об ошибке.
        В случае отсутствия пользователя возвращает сообщение об ошибке.
    GET:
        Возвращает страницу входа.
    Возвращает:
        str: Сообщение об ошибке в случае неудачи.
        Response: Перенаправление на главную страницу или страницу входа.
    """

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        usr = User.query.filter_by(email=email).first()
        if usr:
            # Проверка пароля
            if usr.check_password(password):
                login_user(usr)
                # Перенаправление на страницу профиля
                return redirect('/')
            else:
                return 'Wrong passwd.', 400
        else:
            return 'User do not exist.', 400

        return redirect('/login')

    else:
        return render_template('login.html', **filter_params())
