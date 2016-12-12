# -*- coding: utf-8 -*-
from math import factorial


def p20(n):
    return sum(map(int, str(factorial(n))))


assert p20(10) == 27
print(p20(100))