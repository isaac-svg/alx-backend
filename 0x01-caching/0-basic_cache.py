#!/usr/bin/env python3

"""
 Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class that implements a caching mech
    '''

    def put(self, key, item):
        '''assign to the dictionary `self.cache_data` the
           `item` value for the key `key`
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the value having `key` as key
        Args:
        key(string):
        """

        return self.cache_data.get(key, None)
