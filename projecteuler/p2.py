# -*- coding: utf-8 -*-
from itertools import takewhile

def fibonacci():
    a, b = 0, 1
    
    while b < 4000000:
        yield b
        a, b = b, a + b


def bound(generator, maxN):
    return takewhile(lambda i: i <= maxN, generator)


def p2():
    return sum(i for i in bound(fibonacci(), 4000000) if i & 1 == 0)


print(p2())