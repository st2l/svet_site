from flask import render_template, request, redirect, url_for, flash
from models import db, User
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from helpers import filter_params


def login():
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
                flash('Неверный пароль.', 'error')
        else:
            flash('Пользователь не найден.', 'error')

        return redirect('/login')

    else:
        return render_template('login.html', **filter_params())
