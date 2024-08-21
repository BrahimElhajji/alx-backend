#!/usr/bin/env python3
"""a class LFUCache that inherits from BaseCaching
and is a caching system"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a LFU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.frequency = {}
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:

            self.frequency[key] += 1
            self.order.remove(key)
        else:

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                least_freq = min(self.frequency.values())
                least_freq_keys = [k for k, v in self.frequency.items()
                                   if v == least_freq]

                if len(least_freq_keys) > 1:
                    lru_key = None
                    for k in self.order:
                        if k in least_freq_keys:
                            lru_key = k
                            break
                    least_freq_keys.remove(lru_key)
                    key_to_discard = lru_key
                else:
                    key_to_discard = least_freq_keys[0]

                del self.cache_data[key_to_discard]
                del self.frequency[key_to_discard]
                self.order.remove(key_to_discard)
                print(f"DISCARD: {key_to_discard}")

            self.frequency[key] = 1

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
