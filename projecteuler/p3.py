# -*- coding: utf-8 -*-

def p3(n):
    i = 2

    while True:
        while n % i == 0:
            n /= i

        if n == 1:
            break

        i += 1

    return i


assert p3(13195) == 29
print(p3(600851475143))