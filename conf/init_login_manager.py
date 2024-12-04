from flask_login import LoginManager, UserMixin, current_user
from models import User


def init_login_manager(app):

    # create all needed for loading user
    login_manager = LoginManager()
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))