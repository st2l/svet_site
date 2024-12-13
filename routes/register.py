from flask import render_template, request, redirect, url_for, flash
from models import db, User
import re
from helpers import filter_params


def validate_email(email):
    """
    Проверяет, является ли введенный адрес электронной почты допустимым.
    Аргументы:
        mail (str): Адрес электронной почты для проверки.
    Возвращает:
        bool: True, если адрес электронной почты допустим, иначе False.
    """

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def validate_password(password):
    """
    Проверяет, соответствует ли пароль заданным критериям.
    Аргументы:
    password (str): Пароль для проверки.
    Возвращает:
        bool: True, если пароль соответствует всем критериям, иначе False.
    Критерии:
    - Пароль должен быть хотя бы 8 символов.
    - Пароль должен содержать хотя бы одну цифру.
    - Пароль должен содержать хотя бы одну заглавную букву.
    """

    if len(password) < 8:
        return False  # Пароль должен быть хотя бы 8 символов
    if not re.search(r'\d', password):  # Пароль должен содержать хотя бы одну цифру
        return False
    # Пароль должен содержать хотя бы одну заглавную букву
    if not re.search(r'[A-Z]', password):
        return False
    return True


def register():
    """
    Обрабатывает регистрацию нового пользователя.
    Если метод запроса 'POST', функция выполняет следующие действия:
    1. Получает имя пользователя, email и пароль из формы запроса.
    2. Проверяет, что имя пользователя не пустое.
    3. Проверяет корректность email.
    4. Проверяет, что пароль соответствует требованиям (не менее 8 символов, содержит хотя бы одну цифру и одну заглавную букву).
    5. Проверяет, что пользователь с таким именем пользователя не существует в базе данных.
    6. Создает нового пользователя и сохраняет его в базе данных.
    7. Перенаправляет пользователя на страницу входа.
    Если метод запроса не 'POST', функция возвращает страницу регистрации.
    Returns:
        str: Сообщение об ошибке и код состояния 400, если проверка не пройдена.
        Response: Перенаправление на страницу входа при успешной регистрации.
        Response: Страница регистрации, если метод запроса не 'POST'.
    """


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
        params = filter_params()

        return render_template('register.html', **params)
