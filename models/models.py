from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """
    Класс User представляет пользователя в базе данных.
    Атрибуты:
        id (int): Уникальный идентификатор пользователя.
        username (str): Уникальное имя пользователя.
        email (str): Уникальный адрес электронной почты пользователя.
        password_hash (str): Хэш пароля пользователя.
        created_at (datetime): Дата и время создания пользователя.
        admin (bool): Флаг, указывающий, является ли пользователь администратором.
    Методы:
        set_password(password):
            Хэширует пароль для сохранения в базе данных.
        check_password(password):
            Проверяет пароль на соответствие хэшу.
        __repr__():
            Возвращает строковое представление пользователя.
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        """Хэширует пароль для сохранения в базе данных."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Проверяет пароль на соответствие хэшу."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
