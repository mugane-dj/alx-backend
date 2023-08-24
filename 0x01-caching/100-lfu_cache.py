#!/usr/bin/python3
"""
LFU Cache System
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Inherits from BaseCaching class and overrides put and get method
    using LFU replacement policy
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.freq_dict = {}

    def put(self, key, item):
        """
        The function `put` adds a key-value pair to the `cache_data`
        dictionary.

        :param key: The key parameter is used to identify the item in
                    the cache.
        :param item: The "item" parameter is the value that you want to
                     store in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.freq_dict[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    least_freq_key = min(self.freq_dict, key=self.freq_dict
                                         .get)
                    print("DISCARD: {}".format(least_freq_key))
                    del self.cache_data[least_freq_key]
                    del self.freq_dict[least_freq_key]

                self.cache_data[key] = item
                self.freq_dict[key] = 1
            # print(self.freq_dict)

    def get(self, key):
        """
        The function `get` retrieves the value associated with a given
        key from a cache.

        :param key: The `key` parameter is the key used to retrieve a
                    value from the cache
        :return: The value associated with the given key in the cache_data
                 dictionary is being returned.
        """
        if key in self.cache_data:
            self.freq_dict[key] += 1
            return self.cache_data.get(key)
        return None
