#!/usr/bin/env python3
"""LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache is a caching system with LFU eviction policy
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.cache_order = []
        self.usage_count = {}

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, do nothing
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
        you must discard the least frequency used item (LFU algorithm)
        if you find more than 1 item to discard, you must use the LRU algorithm
        to discard only the least recently used
        you must print DISCARD: with the key discarded and following by a
        new line
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_order.remove(key)
            self.usage_count[key] += 1
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_used_key = min(self.usage_count, key=self.usage_count.get)
            if self.usage_count[key] == self.usage_count[least_used_key]:
                least_used_key = self.cache_order.pop(0)
            else:
                self.cache_order.remove(least_used_key)
            del self.cache_data[least_used_key]
            del self.usage_count[least_used_key]
            print(f"DISCARD: {least_used_key}")

        self.cache_data[key] = item
        self.cache_order.append(key)
        self.usage_count[key] = 1

    def get(self, key):
        """ Get an item by key
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_order.remove(key)
        self.cache_order.append(key)
        self.usage_count[key] += 1
        return self.cache_data[key]
