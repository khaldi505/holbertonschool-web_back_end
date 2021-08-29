#!/usr/bin/env python3
"""
flask app
"""
import flask
from flask import Flask
from flask.globals import request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """
        for now it only returns the
        jsonify message,
        only allow get request
    """
    return flask.jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
        an end point to register a user.

    """
    try:
        user = AUTH.register_user(
            request.form['email'],
            request.form['password']
                )
    except ValueError:
        return flask.jsonify({"message": "email already registered"}), 400
    return flask.jsonify(
        {
            "email": "<registered email>",
            "message": "user created"
            })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
