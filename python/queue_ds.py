class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class ArrayQueue:
    """FIFO queue implementation using a python list as uderlying storage"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if queue is empty"""
        return self._size == 0

    def first(self):
        """Return but don't remove the element in the front of the queue.
        Raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element in the queue.
        Raise Empty exception if empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size = -1
        return answer
