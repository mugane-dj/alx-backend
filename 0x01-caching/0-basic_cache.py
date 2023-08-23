#!/usr/bin/python3
"""
Basic Cache System
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def init(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        The function `put` adds a key-value pair to the `cache_data`
        dictionary.

        :param key: The key parameter is used to identify the item in
                    the cache.
        :param item: The "item" parameter is the value that you want to
                     store in the cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        The function `get` retrieves the value associated with a given
        key from a cache.

        :param key: The `key` parameter is the key used to retrieve a
                    value from the cache
        :return: The value associated with the given key in the cache_data
                 dictionary is being returned.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
