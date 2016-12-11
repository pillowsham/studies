# -*- coding: utf-8 -*-

def p1(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
    

if __name__ == '__main__':
    assert p1(10) == 23

print(p1(1000))