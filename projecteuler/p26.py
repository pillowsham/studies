# -*- coding: utf-8 -*-

def fraction(n):
    a = 1
    while a % n != 0:
        r, a = divmod(10 * a, n)
        yield (r, a)


def recip(x):
    seen = list()
    
    for i in fraction(x):
        if i in seen:
            return (len(seen)-seen.index(i), x)
        seen.append(i)
    
    return (0, x)


def p26(iterable):
    return max(map(recip, iterable))[1]


assert p26(range(2, 11)) == 7
print(p26(range(1, 1001)))