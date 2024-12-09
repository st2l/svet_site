from sqlalchemy.orm import configure_mappers
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_admin import Admin, expose, AdminIndexView
from flask import redirect, url_for, request
from flask_admin.form import FileUploadField
from models import User, Category, SubCategory, SubSubCategory, Lamp
from flask_admin.contrib.sqla import ModelView
import pandas as pd
import os
import requests


def admin_init(app, db):

    # flask-admin configuration

    class MyAdminIndexView(AdminIndexView):
        @expose('/')
        def index(self):
            return self.render('admin/custom_admin.html')
        
        @expose('/merge_excel', methods=['GET', 'POST'])
        def merge_excel(self):
            if request.method == 'POST':
                file = request.files['excel_file']
                if file:
                    df = pd.read_excel(file)
                    self.process_excel_data(df)
            return self.render('admin/merge_excel.html')

        def download_image(self, url, save_path):
            response = requests.get(url)
            if response.status_code == 200:
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                return True
            return False

        def process_excel_data(self, df):
            i = 0
            for _, row in df.iterrows():
                i += 1
                category_name = row['Название раздела']
                subcategory_name = row['Название раздела.1']
                subsubcategory_name = row['Название раздела.2']

                print(i)

                if (not subcategory_name) or (str(subcategory_name) == 'nan'):
                    subcategory_name = category_name
                    subsubcategory_name = category_name
                elif subcategory_name and (not subsubcategory_name or str(subsubcategory_name) == 'nan'):
                    subsubcategory_name = subcategory_name
                


                lamp_data = {
                    'model': row['Модель [PROP_2049]'],
                    'article': row['Артикул [CML2_ARTICLE]'],
                    'availability': row['Метка "Уточнить наличие" [SALE_TEXT]'],
                    'series': row['Серия (коллекция) [SERIA]'],
                    'name': row['Наименование элемента'],
                    'style': row['Стиль [STIL]'],
                    'body_color': row['Цвет корпуса (арматуры) [COLOR_KORP]'],
                    'shade_color': row['Цвет плафона (стекла) [COLOR_PLAT]'],
                    'body_material': row['Материал корпуса (арматуры) [MAT_KOR_AR]'],
                    'shade_material': row['Материал плафона (стекла) [MAT_PL_ST]'],
                    'head_shape': row['Форма "головы" светильника [FORM_GOL]'],
                    'install_type': row['Тип установки [TIP_YS]'],
                    'mount_type': row['Тип крепления [TIP_KREP]'],
                    'bracket_count': row['Количество кронштейнов (консолей) [KOL_KRSH]'],
                    'lamp_count': row['Количество ламп (цоколей) [KOLL_LAMP]'],
                    'socket_type': row['Цоколь [COCOL]'],
                    'lamp_type': row['Тип ламп (основной) [TIP_LAMP_OS]'],
                    'max_power': row['Макс. мощность (для ламп накаливания) [MAX_LAMP_NAK]'],
                    'voltage': row['Напряжение, V [VOLT]'],
                    'ip_protection': row['Степень защиты IP [IP]'],
                    'weight': row['Вес светильника [VES]'],
                    'height': row['Высота светильника [H_SVET]'],
                    'width': row['Ширина светильника [W_SVET]'],
                    'diameter': row['Размер (диаметр) "головы" светильника [RAZMER_D]'],
                    'length': row['Длина светильника [D_SVET]'],
                    'depth': row['Глубина светильника [G_SVET]'],
                    'country': row['Страна производства [S_PROIZV]'],
                    'warranty': row['Гарантия [GARANT]'],
                    'brand': row['Бренд (фабрика) [BRAND]'],
                    'description': row['Детальное описание'],
                    'price': row['Цена "Розничная цена"'],
                    'main_image': row['Детальная картинка (путь)'],
                    'photo1': row['Схема-картинка [MORE_PHOTO2]'],
                    'photo2': row['фото ламп [MORE_PHOTO4]'],
                    'photo3': row['Картика вторая [MORE_PHOTO]'],
                    'photo4': row['доп фото 5 [MORE_PHOTO5]'],
                    'photo5': row['доп фото 6 [MORE_PHOTO3]'],
                    'photo6': row['доп фото 7 [MORE_PHOTO7]'],
                    'photo7': row['доп фото 8 [MORE_PHOTO8]'],
                    'photo8': row['доп фото 9 [MORE_PHOTO9]'],
                    'photo9': row['доп фото 10 [MORE_PHOTO10]'],
                    'photo10': row['доп фото 11 [MORE_PHOTO11]'],
                    'photo11': row['доп фото 11 [MORE_PHOTO11].1'],
                    'photo12': row['доп фото 12 [MORE_PHOTO12]'],
                    'photo13': row['доп фото 13 [MORE_PHOTO13]'],
                    'photo14': row['доп фото 14 [MORE_PHOTO14]'],
                    'photo15': row['доп фото 15 [MORE_PHOTO15]'],
                    'photo16': row['доп фото 16 [MORE_PHOTO16]'],
                    'photo17': row['доп фото 17 [MORE_PHOTO17]'],
                    'photo18': row['доп фото 18 [MORE_PHOTO18]'],
                    'photo19': row['доп фото 19 [MORE_PHOTO19]'],
                    'photo20': row['доп фото 20 [MORE_PHOTO20]']
                }

                for key in ['main_image', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6', 'photo7', 'photo8', 'photo9', 'photo10', 'photo11', 'photo12', 'photo13', 'photo14', 'photo15', 'photo16', 'photo17', 'photo18', 'photo19', 'photo20']:
                    if str(lamp_data[key]) != 'nan':
                        try:
                            filename = f"{key}_{lamp_data['article']}.jpg"
                            save_path = os.path.join('static', 'img', filename)
                            if self.download_image(lamp_data[key], save_path):
                                lamp_data[key] = f"{key}_{lamp_data['article']}.jpg"
                            else:
                                lamp_data[key] = None
                        except Exception as e:
                            lamp_data[key] = None

                category = Category.query.filter_by(name=category_name).first()
                if not category:
                    category = Category(name=category_name)
                    db.session.add(category)
                    db.session.commit()

                subcategory = SubCategory.query.filter_by(name=subcategory_name, category_id=category.id).first()
                if not subcategory:
                    subcategory = SubCategory(name=subcategory_name, category_id=category.id)
                    db.session.add(subcategory)
                    db.session.commit()

                subsubcategory = SubSubCategory.query.filter_by(name=subsubcategory_name, subcategory_id=subcategory.id).first()
                if not subsubcategory:
                    subsubcategory = SubSubCategory(name=subsubcategory_name, subcategory_id=subcategory.id)
                    db.session.add(subsubcategory)
                    db.session.commit()

                lamp = Lamp.query.filter_by(name=lamp_data['name'], subsubcategory_id=subsubcategory.id).first()
                if not lamp:
                    lamp = Lamp(subsubcategory_id=subsubcategory.id, **lamp_data)
                    db.session.add(lamp)
                    db.session.commit()

        def is_accessible(self):
            # Доступ только для авторизованных пользователей
            return current_user.is_authenticated and current_user.admin

        def inaccessible_callback(self, name, **kwargs):
            # Перенаправление на страницу входа, если доступ запрещен
            return redirect(url_for('login'))

    admin = Admin(app, index_view=MyAdminIndexView(),
                  name='Админка', template_mode='bootstrap4')

    class AdminModelView(ModelView):
        column_display_pk = True  # optional, but I like to see the IDs in the list
        column_hide_backrefs = False

        def is_accessible(self):
            # Доступ только для авторизованных пользователей
            return current_user.is_authenticated and current_user.admin

        def inaccessible_callback(self, name, **kwargs):
            # Перенаправление на страницу входа, если доступ запрещен
            return redirect(url_for('login'))

    class CategoryAdmin(AdminModelView):
        column_labels = {
            'id': 'ID',
            'name': 'Название'
        }

    class SubCategoryAdmin(AdminModelView):
        column_labels = {
            'id': 'ID',
            'name': 'Название',
            'category_id': 'ID Категории',
            'category': 'Категория'
        }

    class SubSubCategoryAdmin(AdminModelView):
        column_labels = {
            'id': 'ID',
            'name': 'Название',
            'subcategory_id': 'ID Подкатегории',
            'subcategory': 'Подкатегория'
        }

    class LampView(AdminModelView):
        column_labels = {
            'id': 'ID',
            'subsubcategory_id': 'ID Подподкатегории',
            'subsubcategory': 'Подподкатегория',
            'model': 'Модель',
            'article': 'Артикул',
            'availability': 'Наличие',
            'series': 'Серия',
            'name': 'Наименование',
            'style': 'Стиль',
            'body_color': 'Цвет корпуса',
            'shade_color': 'Цвет плафона',
            'body_material': 'Материал корпуса',
            'shade_material': 'Материал плафона',
            'head_shape': 'Форма головы',
            'install_type': 'Тип установки',
            'mount_type': 'Тип крепления',
            'bracket_count': 'Количество кронштейнов',
            'lamp_count': 'Количество ламп',
            'socket_type': 'Цоколь',
            'lamp_type': 'Тип ламп',
            'max_power': 'Макс. мощность',
            'voltage': 'Напряжение',
            'ip_protection': 'Степень защиты IP',
            'weight': 'Вес',
            'height': 'Высота',
            'width': 'Ширина',
            'diameter': 'Диаметр',
            'length': 'Длина',
            'depth': 'Глубина',
            'country': 'Страна производства',
            'warranty': 'Гарантия',
            'brand': 'Бренд',
            'description': 'Описание',
            'price': 'Цена',
            'main_image': 'Основное изображение',
            'photo1': 'Фото 1',
            'photo2': 'Фото 2',
            'photo3': 'Фото 3',
            'photo4': 'Фото 4',
            'photo5': 'Фото 5',
            'photo6': 'Фото 6',
            'photo7': 'Фото 7',
            'photo8': 'Фото 8',
            'photo9': 'Фото 9',
            'photo10': 'Фото 10',
            'photo11': 'Фото 11',
            'photo12': 'Фото 12',
            'photo13': 'Фото 13',
            'photo14': 'Фото 14',
            'photo15': 'Фото 15',
            'photo16': 'Фото 16',
            'photo17': 'Фото 17',
            'photo18': 'Фото 18',
            'photo19': 'Фото 19',
            'photo20': 'Фото 20'
        }
        form_overrides = {
            'main_image': FileUploadField,
            'photo1': FileUploadField,
            'photo2': FileUploadField,
            'photo3': FileUploadField,
            'photo4': FileUploadField,
            'photo5': FileUploadField,
            'photo6': FileUploadField,
            'photo7': FileUploadField,
            'photo8': FileUploadField,
            'photo9': FileUploadField,
            'photo10': FileUploadField,
            'photo11': FileUploadField,
            'photo12': FileUploadField,
            'photo13': FileUploadField,
            'photo14': FileUploadField,
            'photo15': FileUploadField,
            'photo16': FileUploadField,
            'photo17': FileUploadField,
            'photo18': FileUploadField,
            'photo19': FileUploadField,
            'photo20': FileUploadField,
        }

        # Настройка FileUploadField
        form_args = {
            'main_image': {
                'label': 'Upload Main Image',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo1': {
                'label': 'Upload Photo 1',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo2': {
                'label': 'Upload Photo 2',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo3': {
                'label': 'Upload Photo 3',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo4': {
                'label': 'Upload Photo 4',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo5': {
                'label': 'Upload Photo 5',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo6': {
                'label': 'Upload Photo 6',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo7': {
                'label': 'Upload Photo 7',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo8': {
                'label': 'Upload Photo 8',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo9': {
                'label': 'Upload Photo 9',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo10': {
                'label': 'Upload Photo 10',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo11': {
                'label': 'Upload Photo 11',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo12': {
                'label': 'Upload Photo 12',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo13': {
                'label': 'Upload Photo 13',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo14': {
                'label': 'Upload Photo 14',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo15': {
                'label': 'Upload Photo 15',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo16': {
                'label': 'Upload Photo 16',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo17': {
                'label': 'Upload Photo 17',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo18': {
                'label': 'Upload Photo 18',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo19': {
                'label': 'Upload Photo 19',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
            'photo20': {
                'label': 'Upload Photo 20',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            },
        }

    # MUST HAVE!!!
    configure_mappers()

    admin.add_view(AdminModelView(User, db.session))
    admin.add_view(CategoryAdmin(Category, db.session))
    admin.add_view(SubCategoryAdmin(SubCategory, db.session))
    admin.add_view(SubSubCategoryAdmin(SubSubCategory, db.session))
    admin.add_view(LampView(Lamp, db.session))
