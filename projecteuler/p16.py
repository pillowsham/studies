# -*- coding: utf-8 -*-

def p16(p):
    return sum(map(int, str(2**p)))

assert p16(15) == 26
print(p16(1000))