from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """
    Represents a user in the application.
    
    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user, must be unique and not null.
        email (str): The email address of the user, must be unique and not null.
        password_hash (str): The hashed password of the user, not null.
        created_at (datetime): The timestamp when the user was created, defaults to the current UTC time.
        admin (bool): Indicates whether the user has administrative privileges, defaults to False.
    Methods:
        set_password(password):
            Hashes the given password and stores it in the password_hash attribute.
        check_password(password):
            Checks if the given password matches the stored password hash.
        __repr__():
            Returns a string representation of the user.
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
