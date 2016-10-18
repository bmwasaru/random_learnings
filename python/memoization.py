from functools import lru_cache


@lru_cache(maxsize=2000)
def fibonacci(n):
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    return value

for n in range(1, 50):
    print(n, ":", fibonacci(n))
