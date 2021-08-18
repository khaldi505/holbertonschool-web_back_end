#!/usr/bin/env python3
"""
    basic auth class
    that inherits from auth
"""
from api.v1.auth.auth import Auth
import base64


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
            decoded_base64_authorization_header.split(":")[0],
            decoded_base64_authorization_header.split(":")[1]
        )
