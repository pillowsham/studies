# -*- coding: utf-8 -*-

COUNTS = { 0:0, 1:3,  2:3,  3:5,  4:4,  5:4,  6:3,  7:5,  8:5, 9:4,
          10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,
          20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}

def count(i):
    r = 0

    if i >= 1000:
        r += COUNTS[i // 1000] + 8
        i %= 1000
        if i != 0:
            r += 3
    
    if i >= 100:
        r += COUNTS[i // 100] + 7
        i %= 100
        if i != 0:
            r += 3

    if i in COUNTS:
        r += COUNTS[i]
    else:
        r += COUNTS[(i // 10)*10] + COUNTS[i % 10]

    return r


def p17(n):
    return sum(map(count, range(1, n+1)))


assert p17(5) == 19
print(p17(1000))