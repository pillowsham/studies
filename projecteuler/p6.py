# -*- coding: utf-8 -*-

def p6(n):
    return sum(range(n+1))**2 - sum(i**2 for i in range(n+1))


assert p6(10) == 2640
print(p6(100))