# -*- coding: utf-8 -*-

def p31(s, coins):
    arr = [1] + [0]*s

    for c in coins:
        for i in range(c, s+1):
            arr[i] += arr[i-c]

    return arr[-1]

print(p31(200, [1, 2, 5, 10, 20, 50, 100, 200]))