from itertools import dropwhile

digits = set(map(str, range(1, 10)))


def next_n(i):
    j = 2
    n = str(i)
    while True:
        yield n
        n += str(i * j)
        j += 1


def p38():
    m = 0
    for i in range(1, 10 ** 5):
        n = next(dropwhile(lambda x: len(x) < 9, next_n(i)))
        if len(n) == 9 and set(n) == digits and int(n) > m:
            m = int(n)

    return m


print(p38())
