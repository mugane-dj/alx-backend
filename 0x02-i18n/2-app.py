#!/usr/bin/env python3
"""
Get locale from request
"""
from flask_babel import Babel
from flask import Flask, request, render_template

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


@babel.localeselector
def get_locale() -> str:
    """
    Configure supported languages
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index():
    """Renders index.html"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
