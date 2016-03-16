import asyncio


@asyncio.coroutine
def print_hello(string, delay):
    yield from asyncio.sleep(delay)
    print("Hello from asyncio" + string)

loop = asyncio.get_event_loop()
tasks = [
    asyncio.tasks.Task(print_hello("A", 4)),
    asyncio.tasks.Task(print_hello("B", 2))
]
loop.run_until_complete(asyncio.wait(tasks))
