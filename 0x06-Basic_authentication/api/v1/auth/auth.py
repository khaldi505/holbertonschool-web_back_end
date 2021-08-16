#!/usr/bin/env python3
"""
auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    class docc
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
            salut lbnet
        '''
        return False

    def authorization_header(self, request=None) -> str:
        """
        alaa khir
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        nyes"""
        return None
