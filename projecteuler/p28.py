# -*- coding: utf-8 -*-


def sequence(n):
    s = 24
    j = 2
    while j < n:
        yield s
        s += 16*j + 20
        j += 2


def p28(n):
    return 1 + sum(s for s in sequence(n))


assert p28(5) == 101
print(p28(1001))