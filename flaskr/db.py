from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def close_db(err=None):
    """
    Close the connection to the database

    :param err: error object
    :return:
    """
    db.session.remove()
