from models import User
from models import db
from .config import Config
from datetime import datetime

def create_initial_admin(app, db):

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