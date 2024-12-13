def database_init(app, db):
    """
    Инициализирует базу данных для данного приложения.
    Args:
        app (Flask): Экземпляр Flask приложения.
        db (SQLAlchemy): Экземпляр SQLAlchemy базы данных.
    """

    # database init
    db.init_app(app)

    with app.app_context():
        # creation of administrator
        db.create_all()
