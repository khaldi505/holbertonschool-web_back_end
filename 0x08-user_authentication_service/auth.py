#!/usr/bin/env python3
"""
Auth module:
_hash_password
"""
import bcrypt
from sqlalchemy.orm import exc
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


def _hash_password(password: str) -> bytes:
    """
    _hash_password takes a password arg
    return bytes salted hash of the input password
    """
    if not password:
        return None
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
        generate_uuid:
        return a string representation
        of a new UUID.
    """
    return str(uuid.uuid4())


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
        if user:
            raise(
                ValueError(
                    "User {} already exists".format(
                        self._db.find_user_by(email=email).email))
                    )

    def valid_login(self, email: str, password: str) -> bool:
        """
            valid it the login
            Try locating the user by email.
            If it exists, check the password
            with bcrypt.checkpw. If it matches return True.
            In any other case, return False.
            test
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        create_session: takes the email
        as an argument creates a session
        returns a session_id for the new
        session.
        """
        try:
            if email is None or email == "":
                return None
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        user.session_id = _generate_uuid()
        self._db._session.commit()
        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
            get user from session_id
        """
        try:
            if session_id is None or session_id == "":
                return None
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
            destroy the user's session.
            ofc, using the user_id
        """
        try:
            user = self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
            mthod that takes an email str arg and returns a string
        """
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, reset_token=_generate_uuid())
            return user.reset_token
        except Exception as e:
            raise(ValueError)

    def update_password(self, reset_token: str, password: str) -> None:
        """
            update password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_pwd = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_pwd)
            self._db.update_user(user.id, reset_token=None)
        except Exception as e:
            raise(ValueError)
