# -*- coding: utf-8 -*-
from functools import lru_cache

@lru_cache(maxsize = None)
def collatz(n):
    if n == 1:
        return 1

    if n & 1 == 0:
        return 1 + collatz(n // 2)
    else:
        return 1 + collatz(3*n + 1)


print(sorted(map(lambda i: (collatz(i), i), range(1, 1000001)))[-1][1])