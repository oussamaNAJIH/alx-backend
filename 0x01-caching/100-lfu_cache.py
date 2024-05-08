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
                self.items_frequency[key] = 1  # New item, set frequency to 1
            else:
                min_frequency = min(self.items_frequency.values())
                min_freq_keys = [k for k, v in self.items_frequency.items() if v == min_frequency]
                if len(min_freq_keys) == 1:
                    least_frequently_used_key = min_freq_keys[0]
                    print("DISCARD:", least_frequently_used_key)
                    del self.cache_data[least_frequently_used_key]
                    del self.items_frequency[least_frequently_used_key]
                else:
                    # If there are multiple keys with the same minimum frequency,
                    # we choose the least recently used among them (using LRU)
                    least_frequently_used_key = min_freq_keys[0]
                    for k in min_freq_keys:
                        if self.items_frequency[k] < self.items_frequency[least_frequently_used_key]:
                            least_frequently_used_key = k
                    print("DISCARD:", least_frequently_used_key)
                    del self.cache_data[least_frequently_used_key]
                    del self.items_frequency[least_frequently_used_key]
                
                self.cache_data[key] = item
                self.items_frequency[key] = 1  # New item, set frequency to 1
        else:
            # If key is already in cache, just update the item
            self.cache_data[key] = item
            self.items_frequency[key] += 1  # Increment frequency of existing item


    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.items_frequency[key] += 1
        return self.cache_data[key]
