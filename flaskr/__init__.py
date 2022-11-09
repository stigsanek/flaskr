import os

from flask import Flask


def create_app(test_config: dict = None) -> Flask:
    """
    Create and configure the app

    :param test_config: config
    :return:
    """
    app = Flask(__name__, instance_relative_config=True)
    db_path = os.path.join(app.instance_path, "flaskr.sqlite")
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{db_path}"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    from flaskr.db import db, close_db
    import flaskr.models # noqa F401
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.teardown_appcontext(close_db)

    from flaskr.views import auth, blog
    # apply the blueprints to the app
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")

    return app
