from flask_sqlalchemy import SQLAlchemy
from .models import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)

    def __str__(self):
        return str(self.name)


class SubCategory(db.Model):
    __tablename__ = 'subcategories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)
    category = db.relationship(
        Category, backref='Подкатегории (заполнять не надо)')

    def __str__(self):
        return str(self.name)


class SubSubCategory(db.Model):
    __tablename__ = 'subsubcategories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    subcategory_id = db.Column(db.Integer, db.ForeignKey(
        'subcategories.id'), nullable=False)
    subcategory = db.relationship(
        SubCategory, backref='Подпод категории (заполнять не надо)')

    def __str__(self):
        return str(self.name)


class Lamp(db.Model):
    __tablename__ = 'lamps'

    id = db.Column(db.Integer, primary_key=True)
    subsubcategory_id = db.Column(db.Integer, db.ForeignKey(
        'subsubcategories.id'), nullable=False)
        
    subsubcategory = db.relationship(
        SubSubCategory, backref='Товары (заполнять не надо)')

    model = db.Column(db.String(150), nullable=True)  # Модель
    article = db.Column(db.String(100), nullable=True)  # Артикул
    # Метка "Уточнить наличие"
    availability = db.Column(db.String(100), nullable=True)
    series = db.Column(db.String(150), nullable=True)  # Серия (коллекция)
    name = db.Column(db.String(200), nullable=False)  # Наименование элемента
    style = db.Column(db.String(100), nullable=True)  # Стиль
    body_color = db.Column(db.String(100), nullable=True)  # Цвет корпуса
    shade_color = db.Column(db.String(100), nullable=True)  # Цвет плафона
    body_material = db.Column(
        db.String(100), nullable=True)  # Материал корпуса
    shade_material = db.Column(
        db.String(100), nullable=True)  # Материал плафона
    head_shape = db.Column(db.String(100), nullable=True)  # Форма "головы"
    install_type = db.Column(db.String(100), nullable=True)  # Тип установки
    mount_type = db.Column(db.String(100), nullable=True)  # Тип крепления
    # Количество кронштейнов
    bracket_count = db.Column(db.Integer, nullable=True)
    lamp_count = db.Column(db.Integer, nullable=True)  # Количество ламп
    socket_type = db.Column(db.String(100), nullable=True)  # Цоколь
    lamp_type = db.Column(db.String(100), nullable=True)  # Тип ламп
    max_power = db.Column(db.Float, nullable=True)  # Макс. мощность
    voltage = db.Column(db.Integer, nullable=True)  # Напряжение
    ip_protection = db.Column(
        db.String(10), nullable=True)  # Степень защиты IP
    weight = db.Column(db.Float, nullable=True)  # Вес светильника
    height = db.Column(db.Float, nullable=True)  # Высота
    width = db.Column(db.Float, nullable=True)  # Ширина
    diameter = db.Column(db.Float, nullable=True)  # Размер головы
    length = db.Column(db.Float, nullable=True)  # Длина
    depth = db.Column(db.Float, nullable=True)  # Глубина
    country = db.Column(db.String(100), nullable=True)  # Страна производства
    warranty = db.Column(db.String(50), nullable=True)  # Гарантия
    brand = db.Column(db.String(100), nullable=True)  # Бренд
    description = db.Column(db.Text, nullable=True)  # Детальное описание
    price = db.Column(db.Float, nullable=False)  # Цена
    # Основное изображение
    main_image = db.Column(db.String(255), nullable=True)
    # Дополнительные изображения в JSON формате
    extra_images = db.Column(db.JSON, nullable=True)
