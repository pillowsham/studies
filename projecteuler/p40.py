from functools import reduce
from itertools import count
import operator


def d(x):
    for n in count(1):
        s = str(n)
        l = len(s)
        if x > l:
            x -= l
        else:
            return int(s[x - 1])


def p40():
    return reduce(operator.mul, map(lambda i: d(10 ** i), range(7)), 1)


print(p40())
