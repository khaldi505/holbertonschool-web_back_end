#!/usr/bin/env python3
"""
for now this module do nothing
"""
from api.v1.auth.auth import Auth
import uuid


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
        self.user_id_by_session_id = {session_id: user_id}
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            yes documention
        """
        if type(session_id) is not str:
            return None
        if session_id is None:
            return None
        return self.user_id_by_session_id.get(session_id)
