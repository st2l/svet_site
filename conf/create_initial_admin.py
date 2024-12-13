from models import User
from models import db
from .config import Config
from datetime import datetime


def create_initial_admin(app, db):
    """
    Create an initial admin user if one does not already exist.
    This function checks if a user with the username and email specified in the
    Config class exists in the database. If not, it creates a new admin user
    with the specified credentials and adds it to the database.
    :param app: The Flask application instance.
    :type app: Flask
    :param db: The database instance.
    :type db: SQLAlchemy
    """

    print(Config.ADMIN_NAME, Config.ADMIN_EMAIL, Config.ADMIN_PASSWD)

    with app.app_context():
        if not User.query.filter_by(username=Config.ADMIN_NAME, email=Config.ADMIN_EMAIL).first():
            admin_usr = User(
                username=Config.ADMIN_NAME,
                email=Config.ADMIN_EMAIL,
                created_at=datetime.utcnow(),
                admin=True,
            )
            admin_usr.set_password(Config.ADMIN_PASSWD)
            db.session.add(admin_usr)
            db.session.commit()
