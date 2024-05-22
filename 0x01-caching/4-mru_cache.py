#!/usr/bin/env python3
"""MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache is a caching system with MRU eviction policy
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, do nothing
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
        you must discard the most recently used item (MRU algorithm)
        you must print DISCARD: with the key discarded and
        following by a new line
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.cache_order.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key):
        """ Get an item by key
        If key is None or doesn’t exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_order.remove(key)
        self.cache_order.append(key)
        return self.cache_data[key]
