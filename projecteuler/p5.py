# -*- coding: utf-8 -*-
from functools import reduce
from operator import mul

def p5(n):
    l = list(i for i in range(n + 1))

    for i in range(2, n // 2 + 1):
        for j in range(2*i, n+1, i):
            l[j] //= l[i]

    return reduce(mul, l[1:], 1)

assert p5(10) == 2520
print(p5(20))