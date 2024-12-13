from flask import render_template, request, redirect, url_for, flash
from models import db, User
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from helpers import filter_params


def login():
    """
    Handle the login process for users.
    If the request method is POST, it retrieves the email and password from the form data.
    It then checks if a user with the provided email exists in the database.
    If the user exists, it verifies the password. If the password is correct, the user is logged in
    and redirected to the profile page. If the password is incorrect, it returns a 400 status with
    a 'Wrong passwd.' message. If the user does not exist, it returns a 400 status with a 'User do not exist.' message.
    If the request method is not POST, it renders the login page.

    Returns:
        Response: A redirect to the profile page on successful login, a 400 status with an error message
        on failure, or the login page if the request method is not POST.
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
