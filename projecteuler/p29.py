# -*- coding: utf-8 -*-

def p29(a, b):
    r = set()
    for i in range(2, a+1):
        for j in range(2, b+1):
            r.add(i**j)
    return len(r)


assert p29(5, 5) == 15
print(p29(100, 100))