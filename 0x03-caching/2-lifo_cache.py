#!/usr/bin/python3
"""
placeholder
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        placeholder
    """
    LAST_PUT = ""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        placeholder
        """
        if key is None or item is None:
            return
        if (len(self.cache_data.items()) == BaseCaching.MAX_ITEMS):
            if (key not in self.cache_data.keys()):
                lastItem = self.LAST_PUT
                print("DISCARD:", lastItem)
                self.cache_data.pop(lastItem)

        self.cache_data[key] = item
        self.LAST_PUT = key

    def get(self, key):
        """gets the required element by key"""
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
