#!/usr/bin/env python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initialize the cache.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            self.queue.append(key)
            if len(self.queue) > BaseCaching.MAX_ITEMS:
                discard_key = self.queue.pop(0)
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """ Get an item by key
        """
        if key:
            return self.cache_data.get(key)
