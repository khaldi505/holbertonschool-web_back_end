#!/usr/bin/env python3
"""
basic hello world example
"""
import flask
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    a configuration variable
    """
    LANGUAGES = ['en', 'fr']

@app.route("/", methods=['GET'])
def hello_world():
    """hello world"""
    return render_template('0-index.html')
