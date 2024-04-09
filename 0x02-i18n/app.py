#!/usr/bin/env python3
"""
Flask app
"""
import locale
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel
from datetime import timezone as tmzn
from datetime import datetime
from pytz import timezone
import pytz.exceptions
from typing import (
    Dict,
    Union
)


class Config(object):
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Sje", "locale": "fr", "timezone": "Europe/Portsmouth"},
    2: {"name": "Rihana", "locale": "en", "timezone": "US/Calfornia"},
    3: {"name": "Busta", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Telepathy", "locale": None, "timezone": "Europe/London"},
}

def get_timezone():
    """
    Select and return appropriate timezone
    """
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    dflt = app.config['BABEL_DEFAULT_TIMEZONE']
    return dflt


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
