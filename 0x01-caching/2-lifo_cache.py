#!/usr/bin/env python3
"""a class LIFOCache that inherits from BaseCaching
and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.last_key = key
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f"DISCARD: {self.last_key}")
            del self.cache_data[self.last_key]

        self.last_key = key

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
