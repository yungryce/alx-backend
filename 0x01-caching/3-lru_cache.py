#!/usr/bin/env python3
"""Least-Recently -Used caching module.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache defines a LRU caching system.

    Inherits from BaseCaching and implements a simple Least-Recently-Used (LRU)
    cache policy.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        Cache a key-value pair using LRU policy.

        If the cache exceeds the maximum number of items,
        discard the least recently used item

        Args:
            key (str): The key for the cache entry.
            item (any): The value to cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        Return the value linked to a given key.

        Args:
            key (str): The key for the cache entry.

        Returns:
            The value linked to the key, or None if the key doesn't exist.
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
