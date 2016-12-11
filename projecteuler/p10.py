# -*- coding: utf-8 -*-

def p10(n):
    if n < 2:
        return 0
        
    if n == 2:
        return 2

    maxI = (n-1) // 2    
    primes = [True] * maxI
    for i in range(maxI):
        for j in range(2*i*(i+3)+3, maxI, 2*i+3):
            primes[j] = False
    primes = [2*i+3 for i in range(maxI) if primes[i]]

    return 2 + sum(primes)

assert p10(10) == 17
print(p10(2000000))    