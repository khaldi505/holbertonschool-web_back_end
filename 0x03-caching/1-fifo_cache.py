#!/usr/bin/python3
"""
placeholder
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        placeholderigigigigigigiginhebnmout
    """
    def put(self, key, item):
        if key is None or item is None:
            pass
        if BaseCaching.MAX_ITEMS == len(self.cache_data.keys()):
            print("DISCARD:", list(self.cache_data.items())[0][0])
            self.cache_data.pop(list(self.cache_data.items())[0][0])
        self.cache_data[key] = item

    def get(self, key):
        """gets the required element by key"""
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
