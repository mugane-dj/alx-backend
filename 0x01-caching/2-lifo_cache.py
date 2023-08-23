"""
LIFO Caching System
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching class and overrides put and get method
    using LIFO replacement policy
    """
    def __init__(self):
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
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item = self.cache_data.popitem()
            print("DISCARD: {}".format(item[0]))

    def get(self, key):
        """
        The function `get` retrieves the value associated with a given
        key from a cache.

        :param key: The `key` parameter is the key used to retrieve a
                    value from the cache
        :return: The value associated with the given key in the cache_data
                 dictionary is being returned.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
