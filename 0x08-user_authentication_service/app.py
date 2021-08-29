#!/usr/bin/env python3
"""
flask app
"""
import flask
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
        for now it only returns the
        jsonify message,
        only allow get request
    """
    return flask.jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
