from flaskr import create_app


def test_config():
    """
    Test create_app without passing test config

    :return:
    """
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing
