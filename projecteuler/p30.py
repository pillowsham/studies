# -*- coding: utf-8 -*-


def sequence(p):
    d = 2
    while 10**(d-1) <= d * 9**p:
        yield d
        d += 1


def p30(p):
    return sum (n
        for d in sequence(p)
            for n in range(10**(d-1), 10**d)
                if n == sum(int(i)**p for i in str(n)))


assert p30(4) == 19316
print(p30(5))