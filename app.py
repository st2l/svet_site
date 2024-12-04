from flask import Flask
from routes import register_all_routes
from models import db
from conf import create_initial_admin, init_login_manager, database_init, admin_init, Config


app = Flask(__name__)

# import configuration
app.config.from_object(Config)


# configuration process ...
init_login_manager(app=app)
database_init(app, db)
create_initial_admin(app=app, db=db)
admin_init(app, db)
register_all_routes(app=app)


if __name__ == '__main__':
    app.run(debug=True)
