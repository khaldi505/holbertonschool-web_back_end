#!/usr/bin/env python3
"""
for now this module do nothing
"""
from api.v1.auth.auth import Auth
from models.user import User
from os import getenv
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """
        create an auth session
    """
    email = request.form.get("email", None)
    password = request.form.get("password", None)

    if (email is None or email == ""):
        response = jsonify({"error": "email missing"})
        response.status_code = 400
        return response
    if (password is None or password == ""):
        response = jsonify({"error": "password missing"})
        response.status_code = 400
        return response
    current_user = User.search({"email": email})
    if (len(current_user) == 0 or current_user is None):
        response = jsonify({"error": "no user found for this email"})
        response.status_code = 404
        return response

    if not current_user[0].is_valid_password(password):
        response = jsonify({"error": "wrong password"})
        response.status_code = 401
        return response
    else:
        from api.v1.app import auth
        session_id = auth.create_session(current_user[0].id)
        cookie_name = getenv('SESSION_NAME')
        out = jsonify(current_user[0].to_json())
        out.set_cookie(cookie_name, session_id)
        return out


@app_views.route(
    '/auth_session/logout',
    methods=['DELETE'],
    strict_slashes=False
      )
def logout() -> str:
    """log user out
    """

    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    return jsonify({}), 200
