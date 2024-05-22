#!/usr/bin/env python3
""" LIFO Caching.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Implements fifo caching mechanism"""
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Gets a value by key
        """
        return self.cache_data.get(key, None)
