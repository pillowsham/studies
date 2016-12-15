from functools import reduce
from itertools import permutations


def gen_primes():
    sieve = [True] * (10 ** 5)

    for i in range(10 ** 5):
        if sieve[i]:
            for j in range(2 * i * i + 6 * i + 3, 10 ** 5, 2 * i + 3):
                sieve[j] = False

    return {2} | set(2 * i + 3 for i in range(10 ** 5) if sieve[i])


def p41():
    primes = gen_primes()

    for d in reversed(range(1, 10)):
        for c in permutations(reversed(range(1, d + 1)), d):
            n = reduce(lambda a, e: 10 * a + e, c, 0)
            if all(n % p != 0 for p in primes):
                return n


print(p41())
