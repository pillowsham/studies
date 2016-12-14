from math import factorial


def sequence():
    d = 2
    while 10 ** d < d * factorial(9):
        yield d
        d += 1


r = sum(i
        for d in sequence()
        for i in range(10 ** (d - 1), 10 ** d)
        if i == sum(map(factorial, map(int, str(i)))))

print(r)

