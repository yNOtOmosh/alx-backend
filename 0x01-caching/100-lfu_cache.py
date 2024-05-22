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
        If the number of items in self.cache_data exceeds MAX_ITEMS,
        discard the least frequently used item (LFU algorithm)
        If there's a tie, use LRU algorithm to discard the least recently used
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self._update_usage_order(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict()
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key
        If key is None or doesn't exist, return None
        """
        if key is None or key not in self.cache_data:
            return None
        
        self.frequency[key] += 1
        self._update_usage_order(key)
        
        return self.cache_data[key]

    def _update_usage_order(self, key):
        """ Update the usage order of the cache
        """
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)

    def _evict(self):
        """ Evict the least frequently used item, using LRU to break ties
        """
        min_freq = min(self.frequency.values())
        candidates = [k for k, v in self.frequency.items() if v == min_freq]
        lru_key = None
        for key in self.usage_order:
            if key in candidates:
                lru_key = key
                break
        if lru_key:
            del self.cache_data[lru_key]
            del self.frequency[lru_key]
            self.usage_order.remove(lru_key)
            print(f"DISCARD: {lru_key}")
