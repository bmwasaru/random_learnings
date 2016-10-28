import redis


class RedisQueue(object):
    """Queue with redis backend"""

    def __init__(self, name, namespace='queue', **redis_kwargs):
        self.__db = redis.Redis(**redis_kwargs)
        self.key = '%s:%s' % (namespace, name)

    def qsize(self):
        return self.__db.llen(self.key)

    def empty(self):
        """return True if queue is empty"""
        return self.qsize() == 0

    def put(self, item):
        """put item into the queue"""
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.
        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if item:
            item = item[1]
        return item

    def get_noawait(self):
        """equivalent to get(False)"""
        return self.get(False)


q = RedisQueue('test-queue')
q.put('This is a test')
