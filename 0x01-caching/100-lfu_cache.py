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
                self.items_frequency[key] = 0
            else:
                max_frequency = max(self.items_frequency.values())
                max_freq_keys = [k for k, v in self.items_frequency.items() if v == max_frequency]
                if len(max_freq_keys) == 1:
                    least_recently_used_key = max(self.cache_data, key=self.cache_data.get)
                    print("DISCARD:", least_recently_used_key)
                    del self.cache_data[least_recently_used_key]
                    del self.items_frequency[least_recently_used_key]
                else:
                    least_recently_used_key = max_freq_keys[0]
                    for k in max_freq_keys:
                        if self.items_frequency[k] < self.items_frequency[least_recently_used_key]:
                            least_recently_used_key = k
                    print("DISCARD:", least_recently_used_key)
                    del self.cache_data[least_recently_used_key]
                    del self.items_frequency[least_recently_used_key]
                
                self.cache_data[key] = item
                self.items_frequency[key] = 0

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.items_frequency[key] += 1  # Increment frequency regardless of cache hit or miss
        return self.cache_data[key]
