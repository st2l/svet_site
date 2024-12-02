from flask import render_template, request, redirect, url_for, flash
from models import db, User
import re


def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def validate_password(password):
    if len(password) < 8:
        return False  # Пароль должен быть хотя бы 8 символов
    if not re.search(r'\d', password):  # Пароль должен содержать хотя бы одну цифру
        return False
    # Пароль должен содержать хотя бы одну заглавную букву
    if not re.search(r'[A-Z]', password):
        return False
    return True


def register():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        errors = []

        # Проверка на пустое имя пользователя
        if not username:
            errors.append('Имя пользователя не может быть пустым.')

        # Проверка на корректность email
        if not validate_email(email):
            errors.append('Некорректный формат электронной почты.')

        # Проверка пароля
        if not validate_password(password):
            errors.append(
                'Пароль должен быть минимум 8 символов и содержать хотя бы одну цифру и одну заглавную букву.')

        # the same email cannot be in database!
        if User.query.filter_by(username=username).first():
            errors.append('Пользователь с таким именем уже существует.')

        if errors:
            for error in errors:
                flash(error, 'error')  # Показываем ошибки на странице
            # Перенаправляем на страницу регистрации
            return redirect(url_for('register'))
            

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash('Вы успешно зарегистрировались! Теперь войдите в аккаунт.', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html')
