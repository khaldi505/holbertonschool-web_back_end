#!/usr/bin/env python3
"""
 Parametrize templates
"""
import flask
from flask import Flask, render_template, g, request
from flask_babel import Babel
from flask_babel import refresh


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    a configuration variable
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_user() -> dict:
    """
    get user
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    before request handler
    """
    if get_user() is not None:
        g.user = get_user()
        refresh()


@babel.localeselector
def get_locale():
    """ if a user is logged in, use the locale from the user settings
    """
    if request.args.get('locale'):
        if request.args.get('locale') in Config.LANGUAGES:
            return request.args.get('locale')

    if hasattr(g, "user") and(
                    g.user['locale'] and
                    g.user['locale'] in Config.LANGUAGES
                    ):
        return g.user['locale']

    return request.accept_languages.best_match(['en', 'fr'])


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def hello_world():
    """hello world"""
    return render_template('6-index.html')
