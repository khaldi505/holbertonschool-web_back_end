#!/usr/bin/env python3
"""
    basic auth class
    that inherits from auth
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
import sys


class BasicAuth(Auth):
    """
        for now this class
        litearlly does nothing
        except inherits from auth
    """
    def extract_base64_authorization_header(
        self,
        authorization_header: str
            ) -> str:
        """
        Basic - Base64 part
        """
        if (
            type(authorization_header) != str or
            authorization_header is None or
            authorization_header[0:6] != "Basic "
        ):
            return None
        else:
            return authorization_header[6:len(authorization_header)]

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
            ) -> str:
        """
            decode the value of a base64 string
            that is made by the above function
        """
        if (
            type(base64_authorization_header) != str or
            base64_authorization_header is None
        ):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header
                ).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
            ) -> (str, str):
        """
        why the argument name is this long ?
        """
        if (
            decoded_base64_authorization_header is None or
            type(decoded_base64_authorization_header) is not str or
            ":" not in decoded_base64_authorization_header
                ):
            return (None, None)
        return (
            decoded_base64_authorization_header.split(":", 1)[0],
            decoded_base64_authorization_header.split(":", 1)[1]
        )

    def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str
            ) -> TypeVar('User'):
        """do funny stuff"""
        if (
            user_email is None or
            user_pwd is None or
            type(user_email) is not str or
            type(user_pwd) is not str
                ):
            return None
        user = User()
        search = user.search({"email": user_email, })
        if not search:
            return None
        user = search[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
            current user yes
        """
        if not self.authorization_header(request):
            return None
        header = self.authorization_header(request)

        header = self.extract_base64_authorization_header(header)
        if header is None:
            return None
        dec_header = self.decode_base64_authorization_header(header)
        if dec_header is None:
            return None
        creds = self.extract_user_credentials(dec_header)
        if creds is None:
            return None
        email = self.extract_user_credentials(dec_header)[0]
        pwd = self.extract_user_credentials(dec_header)[1]

        if self.user_object_from_credentials(email, pwd) is None:
            return None
        return self.user_object_from_credentials(email, pwd)
