def database_init(app, db):

    # database init
    db.init_app(app)

    with app.app_context():
        # creation of administrator
        db.create_all()
