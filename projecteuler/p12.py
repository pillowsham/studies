# -*- coding: utf-8 -*-
from itertools import combinations
from functools import reduce, lru_cache


def sequence():
    i = 1
    j = 2
    while True:
        yield i
        i += j
        j += 1


@lru_cache(maxsize=None)
def factors(n):
    r = []

    i = 2
    while n != 1:
        while n % i == 0:
            r.append(i)
            n /= i
        i += 1

    return 1 + len(reduce(set.union, map(lambda i: combinations(r, i), range(len(r))), set()))


def p12(count):
    for i in sequence():
        if factors(i) > count:
            return i


assert p12(5) == 28
print(p12(500))
