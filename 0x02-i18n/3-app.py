#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)

# Instantiate Babel object and configure default locale and timezone
babel = Babel(app)


# Define available languages and default locale
# and timezone in a Config class
class Config:
    """
    configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Use Config to set Babel's default locale and timezone
app.config.from_object(Config)


def get_locale():
    """
    determine the best match with our supported languages
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """
    Renders index.html template
    """
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(debug=True)
