import os
from typing import Union

from dotenv import load_dotenv


class Config:
    """Base config"""
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class ProductionConfig(Config):
    """Config for production"""
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class DevelopmentConfig(Config):
    """Config for development"""
    DEBUG = True
    SECRET_KEY = "dev"


class TestingConfig(Config):
    """Config for testing"""
    TESTING = True
    SECRET_KEY = "test"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


def get_config() -> Union[ProductionConfig, DevelopmentConfig]:
    """
    Get config

    :return: config instance
    """
    load_dotenv()

    if os.getenv("ENV") == "prod":
        return ProductionConfig()

    return DevelopmentConfig()
