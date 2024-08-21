#!/usr/bin/env python3
"""a class LRUCache that inherits from BaseCaching
and is a caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a LRU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:

            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:

            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
