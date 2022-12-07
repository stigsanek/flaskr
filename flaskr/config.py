import os


class BaseConfig:
    """Base config"""
    TESTING = False
    DEBUG = os.getenv("FLASK_DEBUG", False) == "True"
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class TestingConfig:
    """Config for testing"""
    TESTING = True
    SECRET_KEY = "test"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
