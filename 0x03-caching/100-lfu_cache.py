#!/usr/bin/python3
"""
Least frequently used
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        placeholder
    """
    AGE = 0
    AGE_BITS = {}

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
                leastItem = {
                    k: v for k, v in sorted(self.AGE_BITS.items(),
                                            key=lambda item: item[1])
                }
                leastItem = list(leastItem)[0]
                print("DISCARD:", leastItem)
                self.cache_data.pop(leastItem)
                self.AGE_BITS.pop(leastItem)

        self.cache_data[key] = item
        self.AGE += 1
        self.AGE_BITS[key] = self.AGE

    def get(self, key):
        """gets the required element by key"""
        if key not in self.cache_data.keys():
            return None
        else:
            self.AGE += 1
            self.AGE_BITS[key] = self.AGE
            return self.cache_data[key]
