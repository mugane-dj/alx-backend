#!/usr/bin/env python3
"""
Infer appropriate time zone
"""
import pytz
import flask_babel
from flask import Flask, g, request, render_template
from typing import Dict

app = Flask(__name__)
babel = flask_babel.Babel(app)


class Config:
    """
    Babel configs
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
    Configure supported languages
    """
    param_locale = request.args.get("locale", None)
    if param_locale in Config.LANGUAGES:
        return param_locale
    elif g.user:
        locale = g.user.get("locale")
        if locale in Config.LANGUAGES:
            return locale
    elif request.headers.get("locale"):
        return request.headers.get("locale")

    return Config.BABEL_DEFAULT_LOCALE


@babel.timezoneselector
def get_timezone() -> str:
    """
    Configure timezone
    """
    user_timezone = None
    param_timezone = request.args.get("timezone")
    if param_timezone:
        try:
            user_timezone = pytz.timezone(param_timezone)
        except pytz.UnknownTimeZoneError:
            raise pytz.UnknownTimeZoneError

    if not user_timezone and g.user and g.user.get("timezone"):
        try:
            user_timezone = pytz.timezone(g.user.get("timezone"))
        except pytz.UnknownTimeZoneError:
            raise pytz.UnknownTimeZoneError

    return user_timezone or Config.BABEL_DEFAULT_TIMEZONE


def get_user(login_as: int) -> Dict:
    """
    Gets user from users dict
    """
    if login_as is not None and login_as in users:
        return users.get(login_as)
    return None


@app.before_request
def before_request() -> None:
    """
    sets user on flask.g.user
    """
    login_as = request.args.get("login_as")
    user = get_user(int(login_as)) if login_as else None
    setattr(g, "user", user)


@app.route("/")
def index():
    """Renders index.html"""
    home_title = flask_babel.gettext("home_title")
    home_header = flask_babel.gettext("home_header")
    logged_in_as = flask_babel.gettext("logged_in_as")
    not_logged_in = flask_babel.gettext("not_logged_in")
    username = g.user.get("name") if g.user else None
    return render_template(
        "7-index.html",
        home_title=home_title,
        home_header=home_header,
        logged_in_as=logged_in_as,
        not_logged_in=not_logged_in,
        username=username,
    )


if __name__ == "__main__":
    app.run()
