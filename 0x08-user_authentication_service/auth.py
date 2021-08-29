#!/usr/bin/env python3
"""
Auth module:
_hash_password
"""
import bcrypt
from sqlalchemy.sql.sqltypes import Boolean
from db import DB
import argparse
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """
    _hash_password takes a password arg
    return bytes salted hash of the input password
    """
    if not password:
        return None
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
            register_user
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            created_user = self._db.add_user(email, hashed_password)
            return created_user
        raise(ValueError("User " + self._db.find_user_by(email=email).email))

    def valid_login(self, email: str, password: str) -> Boolean:
        """
            valid it the login
            Try locating the user by email.
            If it exists, check the password
            with bcrypt.checkpw. If it matches return True.
            In any other case, return False.
        """
        if not(email and password):
            return False
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
            return True
        return False
