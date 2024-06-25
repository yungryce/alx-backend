#!/usr/bin/env python3
"""Last-In First-Out caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines a LIFO caching system.

    Inherits from BaseCaching and implements a simple Last-In-First-Out (LIFO)
    cache replacement policy.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        # Use OrderedDict to maintain the order of keys
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Cache a key-value pair using LIFO policy.

        If the cache exceeds the maximum number of items, it discards the
        newest item first.

        Args:
            key (str): The key for the cache entry.
            item (any): The value to cache.
        """
        if key is None or item is None:
            return

        # Check if the cache has reached its max capacity
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data.keys():
            # Discard the last item in the dictionary (LIFO behavior)
            last_key, last_value = self.cache_data.popitem()
            print("DISCARD: {}".format(last_key))

        # Add the new item to the cache
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
