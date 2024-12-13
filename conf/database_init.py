def database_init(app, db):
    """
    Initialize the database with the given Flask application.
    This function initializes the database with the provided Flask application
    and creates all database tables within the application context.
    :param app: The Flask application instance.
    :type app: Flask
    :param db: The database instance to be initialized.
    :type db: SQLAlchemy
    """
    

    # database init
    db.init_app(app)

    with app.app_context():
        # creation of administrator
        db.create_all()
