#!/usr/bin/env python3
"""
for now this module do nothing
"""
from api.v1.views.users import create_user
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from os import getenv


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

    def destroy_session(self, request=None):
        """
            destroy the current session,
            log the user out
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not request.form.get(session_id):
            return False
        else:
            user_id = self.user_id_by_session_id(session_id)
            if not user_id:
                return False
            del self.user_id_by_session_id[session_id]
            return True
