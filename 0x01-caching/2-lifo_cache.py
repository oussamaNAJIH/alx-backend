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
        
        if len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
            self.last_item_key = key

        else:
            last_item_index = list(self.cache_data.keys()).index(self.last_item_key)
            self.cache_data.pop(self.last_item_key)
            print("DISCARD: {}".format(self.last_item_key))
            keys_list = list(self.cache_data.keys())
            if last_item_index > 0:
                self.last_item_key = keys_list[last_item_index - 1]
            else:
                self.last_item_key = keys_list[-1]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)

