#!/usr/bin/env python3
""""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache is a caching system with LIFO eviction policy"""

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """Add an item in the cache
        If key or item is None, do nothing
        If the number of items in self.cache_data exceeds MAX_ITEMS,
        discard the last item put in cache (LIFO algorithm)
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
        """Get an item by key
        If key is None or doesn’t exist, return None
        """
        return self.cache_data.get(key, None)
