#!/usr/bin/env python3
"""
basic hello world example
"""
import flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    """hello world"""
    return render_template('0-index.html')
