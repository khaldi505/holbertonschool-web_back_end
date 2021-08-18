#!/usr/bin/env python3
"""
    basic auth class
    that inherits from auth
"""
from api.v1.auth.auth import Auth


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
