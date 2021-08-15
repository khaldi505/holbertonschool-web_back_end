#!/usr/bin/env python3
"""
amazing password being hashed
"""
import bcrypt


def hash_password(password: str):
    """
    i already told u,
    here ur amazing password will be hashed
    """
    password = bytes(password, 'utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())
