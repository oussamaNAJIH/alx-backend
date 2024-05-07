#!/usr/bin/python3
""" MRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.last_used_item = ""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.last_used_item)
                print("DISCARD: {}".format(self.last_used_item))
                self.cache_data[key] = item
        self.cache_data[key] = item
        self.last_used_item = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.last_used_item = key
        return self.cache_data[key]
