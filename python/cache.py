import datetime
import random


class Cache:

    def __init__(self):
        self.cache = {}
        self.max_cache_size = 200

    def __contains__(self, key):
        return key in self.cache

    def update(self, key, value):
        if key not in self.cache and len(self.cache) > self.max_cache_size:
            self.remove_oldest()
        self.cache[key] = {'date_accessed': datetime.datetime.now(),
                           'value': value}

    def remove_oldest(self):
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['date_accessed'] < self.cache[oldest_entry]['date_accessed']:
                oldest_entry = key
        self.cache.pop(oldest_entry)

    @property
    def size(self):
        return len(self.cache)


if __name__ == '__main__':
    keys = ['yelo', 'hi', 'jux', 'juh', 'wer', 'elve']
    s = 'iyir4jbjcdehiie'
    cache = Cache()
    for i, key in enumerate(keys):
        if key in cache:
            continue
        else:
            value = ''.join([random.choice(s) for i in range(20)])
            cache.update(key, value)
        print("#%s iterations, #%s cached entries" % (i+1, cache.size))
    print
