#!/usr/bin/env python3
"""
for now this module do nothing
"""
from flask.globals import current_app
from api.v1.views.users import create_user
from sys import stderr

from flask.wrappers import Response
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from os import getenv
from flask import jsonify, abort, request
from api.v1.views import app_views


class SessionAuth(Auth):
    """
    just inherits from auth
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            session auth
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID.
        """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value.
        """
        cookie_value = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie_value)
        user = User.get(user_id)
        return user


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """
        on the process of fugring out
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
