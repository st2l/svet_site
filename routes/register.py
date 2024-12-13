from flask import render_template, request, redirect, url_for, flash
from models import db, User
import re
from helpers import filter_params


def validate_email(email):
    """
    Validates if the provided email address matches the standard email format.

    Args:
        email (str): The email address to validate.
    Returns:
        bool: True if the email address is valid, False otherwise.
    """

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def validate_password(password):
    """
    Validates the given password based on the following criteria:
    - The password must be at least 8 characters long.
    - The password must contain at least one digit.
    - The password must contain at least one uppercase letter.

    Args:
        password (str): The password to validate.
    Returns:
        bool: True if the password meets all criteria, False otherwise.
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
    Handle user registration.
    This function processes the registration form submitted via POST request.
    It validates the username, email, and password, checks for existing users,
    and creates a new user if all validations pass. If the request method is GET,
    it renders the registration template.

    Returns:
        str: Error message and HTTP status code 400 if validation fails.
        werkzeug.wrappers.Response: Redirect to the login page on successful registration.
        flask.Response: Rendered registration template for GET requests.
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
