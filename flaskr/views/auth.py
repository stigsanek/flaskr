from functools import wraps

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import db
from flaskr.models import User

bp = Blueprint(name="auth", import_name=__name__, url_prefix="/auth")


def login_required(view):
    """
    View decorator that redirects anonymous users to the login page

    :param view: view function
    :return:
    """

    @wraps(view)
    def wrapper(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(*args, **kwargs)

    return wrapper


@bp.before_app_request
def load_logged_in_user():
    """
    If a user id is stored in the session, load the user object from
    the database into 'g.user'

    :return:
    """
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = db.session.query(User).filter(
            User.user_id == user_id
        ).first()


@bp.route("/register", methods=("GET", "POST"))
def register():
    """
    Register a new user.
    Validates that the username is not already taken.
    Hashes the password for security.

    :return: response
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                db.session.add(
                    User(username, generate_password_hash(password))
                )
                db.session.commit()
            except IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """
    Log in a registered user by adding the user id to the session

    :return: response
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        user = db.session.query(User).filter(
            User.username == username
        ).first()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user.password, password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user.user_id
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """
    Clear the current session, including the stored user id

    :return: response
    """
    session.clear()
    return redirect(url_for("index"))
