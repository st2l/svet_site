from flask import Flask, render_template
from routes import register_all_routes
from config import Config
from models import db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, current_user
from models import User
from datetime import datetime
import os
from conf import create_initial_admin


app = Flask(__name__)

# import configuration
app.config.from_object(Config)

# create all needed for loading user
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# database init
db.init_app(app)

with app.app_context():
    # creation of administrator
    db.create_all()

# flask-admin configuration
admin = Admin(app, name='Админка', template_mode='bootstrap4')


class AdminModelView(ModelView):
    def is_accessible(self):
        # Доступ только для авторизованных пользователей
        return current_user.is_authenticated and current_user.admin

    def inaccessible_callback(self, name, **kwargs):
        # Перенаправление на страницу входа, если доступ запрещен
        return redirect(url_for('login'))


admin.add_view(AdminModelView(User, db.session))

# register all routes
create_initial_admin(app=app)
register_all_routes(app=app)


if __name__ == '__main__':
    app.run(debug=True)
