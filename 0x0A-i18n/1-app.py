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
