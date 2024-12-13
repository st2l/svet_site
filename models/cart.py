from flask_sqlalchemy import SQLAlchemy
from .models import db, User
from .lights import Lamp


class CartItem(db.Model):
    """
    Represents an item in the shopping cart.
    
    Attributes:
        id (int): The unique identifier for the cart item.
        user_id (int): The ID of the user who owns the cart item.
        lamp_id (int): The ID of the lamp associated with the cart item.
        amount (int): The quantity of the lamp in the cart.
    Relationships:
        user (User): The user who owns the cart item.
        lamp (Lamp): The lamp associated with the cart item.
    Methods:
        __str__(): Returns a string representation of the cart item.
        __repr__(): Returns a detailed string representation of the cart item.
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
