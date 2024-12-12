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

        # Проверка на пустое имя пользователя
        if not username:
            return 'Username cannot be empty.', 400

        # Проверка на корректность email
        if not validate_email(email):
            return 'Invalid email.', 400

        # Проверка пароля
        if not validate_password(password):
            return 'Password must be at least 8 characters long, contain at least one digit, and at least one uppercase letter.', 400

        # the same email cannot be in database!
        if User.query.filter_by(username=username).first():
            return 'A user with this username already exists.', 400

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect('/login')
    else:
        return render_template('register.html')
