from flask_sqlalchemy import SQLAlchemy
from .models import db, User
from .lights import Lamp


class CartItem(db.Model):
    """
    Класс, представляющий элемент корзины.
    Атрибуты:
        id (int): Уникальный идентификатор элемента корзины.
        user_id (int): Идентификатор пользователя, которому принадлежит элемент корзины.
        lamp_id (int): Идентификатор лампы, добавленной в корзину.
        amount (int): Количество ламп в корзине (по умолчанию 1).
        user (User): Связь с моделью пользователя.
        lamp (Lamp): Связь с моделью лампы.
    Методы:
        __str__(): Возвращает строковое представление элемента корзины.
        __repr__(): Возвращает строковое представление объекта CartItem для отладки.
    """

    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lamp_id = db.Column(db.Integer, db.ForeignKey('lamps.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False, default=1)

    user = db.relationship(User, backref='cart_items')
    lamp = db.relationship(Lamp, backref='cart_items')

    def __str__(self):
        return 'Элемент корзины'

    def __repr__(self):
        return f'<CartItem {self.id}>'
