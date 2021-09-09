#!/usr/bin/env python3
"""
 Parametrize templates
"""
import flask
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    a configuration variable
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """ if a user is logged in, use the locale from the user settings
    """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(['en', 'fr'])


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def hello_world():
    """hello world"""
    return render_template('3-index.html')
