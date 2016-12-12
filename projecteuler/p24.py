# -*- coding: utf-8 -*-

from itertools import permutations


# return i-th r length permutation of elements in iterable
def permutation(iterable, i, r = None):
    counter = 1

    for p in permutations(iterable, r):
        if counter == i:
            return p

        counter += 1

    return None


print("".join(map(str, permutation(range(10), 1000000))))