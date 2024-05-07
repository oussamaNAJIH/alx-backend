#!/usr/bin/python3
""" LIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.last_item_key = ""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        
        if key not in self.cache_data:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item

            else:
                if not 
                last_item_key = list(self.cache_data.keys())[-1]
                self.cache_data.pop(last_item_key)
                print("DISCARD: {}".format(last_item_key))
        else:
            self.cache_data[key] = item
            self.last_item_key = key

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
