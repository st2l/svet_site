from flask_login import LoginManager, UserMixin, current_user
from models import User


def init_login_manager(app):

    # create all needed for loading user
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        """
        Load a user from the database by user ID.
        :param user_id: The ID of the user to load.
        :type user_id: int
        :return: The user object if found, otherwise None.
        :rtype: User or None
        """

        return User.query.get(int(user_id))
