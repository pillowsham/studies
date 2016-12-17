def trigonal():
    n = 1
    while True:
        yield n * (n + 1) // 2
        n += 1


def pentagonal():
    n = 1
    while True:
        yield n * (3 * n - 1) // 2
        n += 1


def hexagonal():
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1


def p45():
    seq3 = trigonal()
    seq5 = pentagonal()
    seq6 = hexagonal()

    n3 = next(seq3)
    n5 = next(seq5)
    n6 = next(seq6)

    r = []
    while len(r) < 3:
        if n3 == n5 == n6:
            r.append(n3)
            n3 = next(seq3)

        if n3 < n5 or n3 < n6:
            n3 = next(seq3)

        if n5 < n3 or n5 < n6:
            n5 = next(seq5)

        if n6 < n3 or n6 < n5:
            n6 = next(seq6)

    return r[-1]


print(p45())
