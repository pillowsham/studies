from math import gcd
from functools import reduce


def tuple_mul(t1, t2):
    return t1[0] * t2[0], t1[1] * t2[1]


fs = list((a, c)
          for a in range(1, 9)
          for c in range(a + 1, 10)
          for b in range(10)
          if c * (10 * a + b) == a * (10 * b + c))

num, denom = reduce(tuple_mul, fs, (1, 1))
print(denom // gcd(num, denom))
