#!/usr/bin/python3
""""
importing self.cache_data
dictionary from the parent class BaseCaching
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        a class BasicCache that inherits from BaseCaching
        and is a caching system
    """
    def put(self, key, item):
        """"
            Must assign to the dictionary
            self.cache_data the item value for the key key.
            If key or item is None, this method should not do anything.
        """
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """gets the required element by key"""
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
