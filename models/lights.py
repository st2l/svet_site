from flask_sqlalchemy import SQLAlchemy
from .models import db


class Category(db.Model):
    """
    Category model representing a category of lights.
    
    Attributes:
        id (int): Unique identifier for the category.
        name (str): Name of the category, must be unique and not null.
    Methods:
        __str__(): Returns the string representation of the category name.
    """

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)

    def __str__(self):
        return str(self.name)


class SubCategory(db.Model):
    """
    SubCategory model representing a subcategory in the database.

    Attributes:
        id (int): Primary key of the subcategory.
        name (str): Name of the subcategory, must be unique and not null.
        category_id (int): Foreign key referencing the id of the category.
        category (Category): Relationship to the Category model.
    Methods:
        __str__(): Returns the name of the subcategory as a string.
    """

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
    """
    SubSubCategory model represents a sub-subcategory in the database.

    Attributes:
        id (int): Primary key of the sub-subcategory.
        name (str): Name of the sub-subcategory, must be unique and not nullable.
        subcategory_id (int): Foreign key referencing the id of the subcategory.
        subcategory (SubCategory): Relationship to the SubCategory model.
    Methods:
        __str__(): Returns the name of the sub-subcategory as a string.
    """

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
    """
    Represents a Lamp entity in the database.

    Attributes:
        id (int): Primary key.
        subsubcategory_id (int): Foreign key referencing SubSubCategory.
        subsubcategory (SubSubCategory): Relationship to SubSubCategory.
        model (str): Model of the lamp.
        article (str): Article number.
        availability (str): Availability status.
        series (str): Series or collection.
        name (str): Name of the lamp.
        style (str): Style of the lamp.
        body_color (str): Color of the lamp body.
        shade_color (str): Color of the lamp shade.
        body_material (str): Material of the lamp body.
        shade_material (str): Material of the lamp shade.
        head_shape (str): Shape of the lamp head.
        install_type (str): Installation type.
        mount_type (str): Mounting type.
        bracket_count (str): Number of brackets.
        lamp_count (str): Number of lamps.
        socket_type (str): Socket type.
        lamp_type (str): Type of lamps.
        max_power (str): Maximum power.
        voltage (str): Voltage.
        ip_protection (str): IP protection rating.
        weight (str): Weight of the lamp.
        height (str): Height of the lamp.
        width (str): Width of the lamp.
        diameter (str): Diameter of the lamp head.
        length (str): Length of the lamp.
        depth (str): Depth of the lamp.
        country (str): Country of manufacture.
        warranty (str): Warranty period.
        brand (str): Brand of the lamp.
        description (str): Detailed description.
        price (float): Price of the lamp.
        main_image (str): URL of the main image.
        photo1 (str): URL of additional image 1.
        photo2 (str): URL of additional image 2.
        photo3 (str): URL of additional image 3.
        photo4 (str): URL of additional image 4.
        photo5 (str): URL of additional image 5.
        photo6 (str): URL of additional image 6.
        photo7 (str): URL of additional image 7.
        photo8 (str): URL of additional image 8.
        photo9 (str): URL of additional image 9.
        photo10 (str): URL of additional image 10.
        photo11 (str): URL of additional image 11.
        photo12 (str): URL of additional image 12.
        photo13 (str): URL of additional image 13.
        photo14 (str): URL of additional image 14.
        photo15 (str): URL of additional image 15.
        photo16 (str): URL of additional image 16.
        photo17 (str): URL of additional image 17.
        photo18 (str): URL of additional image 18.
        photo19 (str): URL of additional image 19.
        photo20 (str): URL of additional image 20.
    """

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
    bracket_count = db.Column(db.String(100), nullable=True)
    lamp_count = db.Column(db.String(100), nullable=True)  # Количество ламп
    socket_type = db.Column(db.String(100), nullable=True)  # Цоколь
    lamp_type = db.Column(db.String(100), nullable=True)  # Тип ламп
    max_power = db.Column(db.String(100), nullable=True)  # Макс. мощность
    voltage = db.Column(db.String(100), nullable=True)  # Напряжение
    ip_protection = db.Column(
        db.String(10), nullable=True)  # Степень защиты IP
    weight = db.Column(db.String(100), nullable=True)  # Вес светильника
    height = db.Column(db.String(100), nullable=True)  # Высота
    width = db.Column(db.String(100), nullable=True)  # Ширина
    diameter = db.Column(db.String(100), nullable=True)  # Размер головы
    length = db.Column(db.String(100), nullable=True)  # Длина
    depth = db.Column(db.String(100), nullable=True)  # Глубина
    country = db.Column(db.String(100), nullable=True)  # Страна производства
    warranty = db.Column(db.String(50), nullable=True)  # Гарантия
    brand = db.Column(db.String(100), nullable=True)  # Бренд
    description = db.Column(db.Text, nullable=True)  # Детальное описание
    price = db.Column(db.Float, nullable=False)  # Цена
    # Основное изображение
    main_image = db.Column(db.String(255), nullable=True)

    # additional images
    photo1 = db.Column(db.String(255), nullable=True)
    photo2 = db.Column(db.String(255), nullable=True)
    photo3 = db.Column(db.String(255), nullable=True)
    photo4 = db.Column(db.String(255), nullable=True)
    photo5 = db.Column(db.String(255), nullable=True)
    photo6 = db.Column(db.String(255), nullable=True)
    photo7 = db.Column(db.String(255), nullable=True)
    photo8 = db.Column(db.String(255), nullable=True)
    photo9 = db.Column(db.String(255), nullable=True)
    photo10 = db.Column(db.String(255), nullable=True)
    photo11 = db.Column(db.String(255), nullable=True)
    photo12 = db.Column(db.String(255), nullable=True)
    photo13 = db.Column(db.String(255), nullable=True)
    photo14 = db.Column(db.String(255), nullable=True)
    photo15 = db.Column(db.String(255), nullable=True)
    photo16 = db.Column(db.String(255), nullable=True)
    photo17 = db.Column(db.String(255), nullable=True)
    photo18 = db.Column(db.String(255), nullable=True)
    photo19 = db.Column(db.String(255), nullable=True)
    photo20 = db.Column(db.String(255), nullable=True)
