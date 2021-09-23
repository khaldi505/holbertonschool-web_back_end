#!/usr/bin/env python3
"""
    Cache class that stores instance of the redis
    client as a private variable named
    _redis using redis.Redist()
    and flush the instance using flushdb.
"""
import redis
import uuid
from typing import Union


class Cache():
    """
    """
    def __init__(self):
        """
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
