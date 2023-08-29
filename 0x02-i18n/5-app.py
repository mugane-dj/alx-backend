#!/usr/bin/env python3
"""
Flask web application
"""
from flask_babel import Babel, gettext
from flask import Flask, g, request, render_template
from typing import Dict

app = Flask(__name__)
babel = Babel(app)


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
def get_locale():
    """
    Configure supported languages
    """
    user_locale = request.args.get("locale")
    if user_locale in Config.LANGUAGES:
        return user_locale
    return request.accept_languages.best_match(Config.LANGUAGES)


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
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    logged_in_as = gettext("logged_in_as")
    not_logged_in = gettext("not_logged_in")
    username = g.user.get("name") if g.user else None
    return render_template(
        "5-index.html",
        home_title=home_title,
        home_header=home_header,
        logged_in_as=logged_in_as,
        not_logged_in=not_logged_in,
        username=username,
    )


if __name__ == "__main__":
    app.run()
