#!/usr/bin/env python3
"""
    Cache class that stores instance of the redis
    client as a private variable named
    _redis using redis.Redist()
    and flush the instance using flushdb.
"""
import redis
import uuid
from typing import Callable, Union, Optional


class Cache():
    """
    """
    def __init__(self):
        """
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get_str(self, key: bytes):
        """
            get data convert data to string
        """
        return key.decode("utf-8")

    def get_int(self, data: bytes):
        """
            get data and convert to int
        """
        return int(data.decode())

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """
            get
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data
