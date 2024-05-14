#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Instantiate Babel object and configure default locale and timezone
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)


@app.route("/")
def index():
    """
    Renders index.html template
    """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(debug=True)
