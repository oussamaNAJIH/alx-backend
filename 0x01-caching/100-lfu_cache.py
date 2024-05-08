#!/usr/bin/python3
""" MRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system.
    """
    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.items_frequency = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.items_frequency[key] = 1
            else:
                min_frequency = min(self.items_frequency.values())
                min_freq_keys = []
                for k, v in self.items_frequency.items():
                    if v == min_frequency:
                        min_freq_keys.append(k)
                if len(min_freq_keys) == 1:
                    least_frequently_used_key = min_freq_keys[0]
                    print("DISCARD:", least_frequently_used_key)
                    del self.cache_data[least_frequently_used_key]
                    del self.items_frequency[least_frequently_used_key]
                else:
                    least_frequently_used_key = min_freq_keys[0]
                    for k in min_freq_keys:
                        myList = self.items_frequency
                        least_frequency = myList[least_frequently_used_key]
                        if self.items_frequency[k] < least_frequency:
                            least_frequently_used_key = k
                    print("DISCARD:", least_frequently_used_key)
                    del self.cache_data[least_frequently_used_key]
                    del self.items_frequency[least_frequently_used_key]

                self.cache_data[key] = item
                self.items_frequency[key] = 1
        else:
            self.cache_data[key] = item
            self.items_frequency[key] += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.items_frequency[key] += 1
        return self.cache_data[key]
