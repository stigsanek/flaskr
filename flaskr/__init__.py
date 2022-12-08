from flask import Flask
from flaskr.config import BaseConfig


def create_app(config=BaseConfig()) -> Flask:
    """
    Create and configure the app

    :param config: config instance
    :return:
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    # register the database commands
    import flaskr.models  # noqa F401
    from flaskr.db import close_db, db
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
