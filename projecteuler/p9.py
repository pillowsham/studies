# -*- coding: utf-8 -*-

def p9():
    for a in range(1,1000):
        for b in range(a+1, 1000):
            if 2*a*b + 10**6 == 2*(a+b)*10**3:
                return a*b*(1000-(a+b))

print(p9())