#!/usr/bin/env python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache is a caching system with LRU eviction policy"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """Add an item in the cache
        If key or item is None, do nothing
        If the number items self.cache_data higher BaseCaching.MAX_ITEMS:
        must discard the least recently used item (LRU algorithm)
        must print DISCARD: with key discarded and following by a new line
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.cache_order.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key):
        """Get an item by key
        If key is None or doesn’t exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_order.remove(key)
        self.cache_order.append(key)
        return self.cache_data[key]
