"""
LRU Caching System
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Inherits from BaseCaching class and overrides put and get method
    using LRU replacement policy
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.lru_order = []

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
                self.lru_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_used_key = self.lru_order.pop(0)
                print("DISCARD: {}".format(least_used_key))
                del self.cache_data[least_used_key]

            self.cache_data[key] = item
            self.lru_order.append(key)

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
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data[key]
        return None
