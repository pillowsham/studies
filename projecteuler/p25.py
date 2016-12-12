# -*- coding: utf-8 -*-

def fibonacci():
    a, b, i = 0, 1, 1
    while True:
        yield (i, b)
        a, b = b, a+b
        i += 1

def p25(n):
    for i, f in fibonacci():
        if len(str(f)) >= n:
            return i

assert p25(3) == 12
print(p25(1000))