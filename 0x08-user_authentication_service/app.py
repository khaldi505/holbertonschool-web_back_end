#!/usr/bin/env python3
"""
flask app
"""
import flask
from flask import Flask, redirect, url_for
from flask.globals import request
from flask.helpers import make_response
from flask.json import jsonify
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
            "email": request.form['email'],
            "message": "user created"
            })


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
        logs you in ?
    """
    email = request.form['email']
    pwd = request.form['password']
    v_login = AUTH.valid_login(email, pwd)

    if (email and pwd and v_login):
        session_id = AUTH.create_session(request.form['email'])
        json_payload = {"email": request.form['email'], "message": "logged in"}
        resp = make_response(json_payload)
        resp.set_cookie('session_id', session_id)
        return resp
    flask.abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
        logout: as the name might suggest ?
    """
    session_id = request.cookies.get('session_id')
    if not (session_id or AUTH.get_user_from_session_id(session_id)):
        flask.abort(403)
    AUTH.destroy_session(session_id)
    return redirect(url_for('index'))


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
    gets profile
    """
    user = AUTH.get_user_from_session_id(request.cookies.get('session_id'))
    if user:
        return jsonify({'email': '{}'.format(user.email)})
    else:
        flask.abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
