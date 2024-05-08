#!/usr/bin/python3
""" LRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.list_item = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.list_item.append(key)

        else:
            if key not in self.cache_data:
                self.cache_data.pop(self.list_item[0])
                print("DISCARD: {}".format(self.list_item[0]))
                del self.list_item[0]
                self.list_item.append(key)
            else:
                self.list_item.remove(key)
                self.list_item.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.list_item.remove(key)
        self.list_item.append(key)
        return self.cache_data[key]
