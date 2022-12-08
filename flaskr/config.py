import os


class BaseConfig:
    """Base config"""
    TESTING = False
    DEBUG = os.getenv("FLASK_DEBUG", True)
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "FLASK_DATABASE_URL", "sqlite:///flaskr.sqlite"
    )


class TestingConfig:
    """Config for testing"""
    TESTING = True
    SECRET_KEY = "test"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
