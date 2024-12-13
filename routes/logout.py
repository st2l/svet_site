from flask import render_template, request, redirect, url_for, flash
from models import db, User
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user


def logout():
    """
    Logs out the current user and redirects to the home page.
    This function logs out the currently authenticated user by calling the
    `logout_user` function and then redirects the user to the root URL ('/').
    
    Returns:
        werkzeug.wrappers.Response: A redirect response to the home page.
    """
    
    logout_user()
    return redirect('/')
