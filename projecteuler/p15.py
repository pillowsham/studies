# -*- coding: utf-8 -*-
from math import factorial

def p15(n, m):
    return factorial(n+m) // (factorial(n) * factorial(m))

assert p15(2, 2) == 6
print(p15(20, 20))