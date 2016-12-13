# -*- coding: utf-8 -*-
from functools import lru_cache
from itertools import takewhile


@lru_cache(maxsize=None)
def is_prime(n):
    if n < 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False

    def squaregt(i):
        return i*i <= n

    return all(n % i != 0 for i in takewhile(squaregt, range(3, n, 2)))


def count(a, b):
    def primecheck(x):
        return is_prime(x*x + a*x + b)
    return len(list(takewhile(primecheck, range(1000))))


arange = range(-999, 1000)
brange = range(1, 1001)


print(max((count(a, b), a*b) for a in arange for b in brange if is_prime(b))[-1])