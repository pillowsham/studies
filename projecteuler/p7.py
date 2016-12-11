# -*- coding: utf-8 -*-

# size of array preseeded to find primes
SIZE = 100001

def p7(n):
    if n <= 3:
        return n

    primes = [True] * SIZE
    for i in range(n+1):
        for j in range(2*i*(i+3)+3, SIZE, 2*i+3):
            primes[j] = False
    primes = [2*i+3 for i in range(SIZE) if primes[i]]

    return primes[n-2]

assert p7(6) == 13
print(p7(10001))
