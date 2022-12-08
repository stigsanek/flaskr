from datetime import datetime

from flaskr.db import db


class User(db.Model):
    """
    User model
    """
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.VARCHAR)
    posts = db.relationship("Post", backref="user")

    def __init__(self, username: str, password: str):
        """
        Initialization

        :param username: username
        :param password: password
        """
        self.username = username
        self.password = password


class Post(db.Model):
    """
    Post model
    """
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    created = db.Column(db.DateTime, default=datetime.now)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.VARCHAR, nullable=False)

    def __init__(self, author_id: int, title: str, body: str):
        """
        Initialization

        :param author_id: user id on author
        :param title: post title
        :param body: post body
        """
        self.author_id = author_id
        self.title = title
        self.body = body
