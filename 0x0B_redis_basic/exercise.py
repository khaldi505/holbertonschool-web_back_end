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
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    """
    key = method.__qualname__
    """
    the key variable
    will hold the name
    of the method used
    to increment the count calls
    later on
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    store the history of inputs and
    outputs for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush("{}:outputs".format(
            method.__qualname__), str(result))
        return result
    return(wrapper)


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

    @call_history
    @count_calls
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
