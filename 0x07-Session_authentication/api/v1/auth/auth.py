#!/usr/bin/env python3
"""
auth
"""
import os
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class Doc
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
            Define which routes don't need authentication
        '''
        if excluded_paths is None or excluded_paths == []:
            return True
        if path and not (
            path in excluded_paths or path + "/" in excluded_paths) or (
            not path
                ):
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """
        Request validation!
        """
        if request is None or ("Authorization" not in request.headers):
            return None

        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        nyes"""
        return None

    def session_cookie(self, request=None):
        """
            Session cookie Capeesh ?
        """
        if request is None:
            return None

        s_name = os.getenv("SESSION_NAME")
        s_id = request.cookies.get(s_name)

        return s_id
