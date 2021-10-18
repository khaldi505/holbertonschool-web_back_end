#!/usr/bin/env python3
"""
    Cache class that stores instance of the redis
    client as a private variable named
    _redis using redis.Redist()
    and flush the instance using flushdb.
"""

import redis
import requests
from functools import wraps
from typing import Callable

_redis = redis.Redis()


def counter(method: Callable) -> Callable:
    """
    """
    @wraps(method)
    def wrapper(url):
        Urlkey = url + "key"
        if _redis.get(Urlkey):
            return _redis.get(Urlkey).decode("utf-8")
        _redis.incr("count:{}".format(url))
        result = method(url)
        _redis.set(Urlkey, result)
        _redis.expire(Urlkey, 10)

        return result
    return(wrapper)


@counter
def get_page(url: str) -> str:
    """
    """
    return requests.get(url).text
