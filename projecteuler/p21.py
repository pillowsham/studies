# -*- coding: utf-8 -*-
from functools import lru_cache


@lru_cache(maxsize=None)
def d(n):
    def is_divisor(i):
        return n % i == 0

    return 1 + sum(filter(is_divisor, range(2, n)))


def is_amicable_pair(x):
    i, j = x
    return i != j and i == d(j)


amicable_numbers = set([x[0] for x in filter(is_amicable_pair, map(lambda i: (i, d(i)), range(1, 10000)))])
print(sum(amicable_numbers))