from sqlalchemy.orm import configure_mappers
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_admin import Admin
from flask_admin.form import FileUploadField
from models import User, Category, SubCategory, SubSubCategory, Lamp


def admin_init(app, db):

    # flask-admin configuration
    admin = Admin(app, name='Админка', template_mode='bootstrap4')

    class AdminModelView(ModelView):
        column_display_pk = True  # optional, but I like to see the IDs in the list
        column_hide_backrefs = False

        def is_accessible(self):
            # Доступ только для авторизованных пользователей
            return current_user.is_authenticated and current_user.admin

        def inaccessible_callback(self, name, **kwargs):
            # Перенаправление на страницу входа, если доступ запрещен
            return redirect(url_for('login'))

    class LampView(AdminModelView):
        form_overrides = {
            'main_image': FileUploadField
        }

        # Настройка FileUploadField
        form_args = {
            'main_image': {
                'label': 'Upload Image',
                'base_path': app.config['UPLOAD_FOLDER'],
                'allowed_extensions': {'png', 'jpg', 'jpeg', 'gif'}
            }
        }

    # MUST HAVE!!!
    configure_mappers()

    admin.add_view(AdminModelView(User, db.session))
    admin.add_view(AdminModelView(Category, db.session))
    admin.add_view(AdminModelView(SubCategory, db.session))
    admin.add_view(AdminModelView(SubSubCategory, db.session))
    admin.add_view(LampView(Lamp, db.session))
