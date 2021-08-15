#!/usr/bin/env python3
"""
amazing password being hashed
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    i already told u,
    here ur amazing password will be hashed
    """
    password = bytes(password, 'utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        let's check if the password hash matches
    """
    if bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password):
        return True
    else:
        return False
