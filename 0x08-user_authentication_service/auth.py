#!/usr/bin/env python3
"""
Auth module:
_hash_password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    _hash_password takes a password arg
    return bytes salted hash of the input password
    """
    if not password:
        return None
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
