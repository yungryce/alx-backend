#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system.

    Inherits from BaseCaching and implements a simple First-In-First-Out (FIFO)
    cache replacement policy.
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method.
        Also initializes an order list to keep track of the insertion order
        of keys.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Cache a key-value pair using FIFO policy.

        If the cache exceeds the maximum number of items, it discards the
        oldest item first.

        Args:
            key (str): The key for the cache entry.
            item (any): The value to cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data.keys():
            # first_key, _ = self.cache_data.popitem(False)
            first_key = next(iter(self.cache_data.keys()))
            del self.cache_data[first_key]
            print("DISCARD: {}". format(first_key))

        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key.

        Args:
            key (str): The key for the cache entry.

        Returns:
            The value linked to the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key, None)
