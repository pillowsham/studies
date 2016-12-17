def pentagonal(x):
    return x * (3 * x - 1) // 2


SIZE = 10000
cache = {pentagonal(i) for i in range(1, SIZE + 1)}


def p44():
    for i in range(1, SIZE):
        pi = pentagonal(i)
        for j in range(i + 1, SIZE + 1):
            pj = pentagonal(j)
            pd = pj - pi
            ps = pj + pi
            if pd in cache and ps in cache:
                return pd


print(p44())
