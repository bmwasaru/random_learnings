from threading import Thread
from time import sleep


def print_hello(string, delay):
    sleep(delay)
    print("Hello from thread:" + string)

ts = [
    Thread(target=print_hello, args=("A", 4)),
    Thread(target=print_hello, args=("B", 2))
]

[t.start() for t in ts]
[t.join() for t in ts]
