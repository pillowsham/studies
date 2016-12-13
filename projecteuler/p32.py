# -*- coding: utf-8 -*-
from functools import reduce
from itertools import permutations


def rem(l1, l2):
    return set(e for e in l1 if e not in l2)


def to_number(t):
    return reduce(lambda acc, i: 10 * acc + i, t, 0)


ns = set()
digits1 = list(range(1, 10))


for d1 in range(1, 5):
    for c1 in permutations(digits1, d1):
        n1 = to_number(c1)
        digits2 = rem(digits1, c1)

        for d2 in range(1, 7-d1):
            if d1 + d2 >= 7:
                break
            
            for c2 in permutations(digits2, d2):
                n2 = to_number(c2)

                n3 = n1*n2
                if len(str(n3)) != 9 - d1 -d2:
                    continue

                digits3 = rem(digits2, c2)
                if digits3 == set(map(int, str(n3))):
                    ns.add(n3)

print(sum(ns))