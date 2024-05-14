#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask_babel import Babel, _
from flask import Flask, render_template, request, g

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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Use Config to set Babel's default locale and timezone
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages
    """
    lang = request.args.get("locale")
    if lang and lang in Config.LANGUAGES:
        return lang
    return request.accept_languages.best_match(Config.LANGUAGES)


# babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """
    Renders index.html template
    """
    return render_template("5-index.html", user=g.user)


def get_user():
    """
    returns a user dictionary or None if the ID cannot
    be found or if login_as was not passed
    """
    id = request.args.get('login_as')
    if id and int(id) in users.keys():
        return users[int(id)]
    return None


@app.before_request
def before_request():
    """
     use get_user to find a user if any,
     and set it as a global on flask.g.user
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run(debug=True)
