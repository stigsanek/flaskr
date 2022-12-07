from flaskr import create_app
from flaskr.config import TestingConfig


def test_config():
    """
    Test create_app without passing test config

    :return:
    """
    assert create_app(TestingConfig()).testing
