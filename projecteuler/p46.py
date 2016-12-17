SIZE = 10000


def p46():
    squares = {i * i for i in range(SIZE)}
    sieve = [True] * SIZE

    for i in range(SIZE):
        if sieve[i]:
            for j in range(2 * i * i + 6 * i + 3, SIZE, 2 * i + 3):
                sieve[j] = False

    primes, composites = [1], []

    for i in range(SIZE):
        n = 2 * i + 3
        if sieve[i]:
            primes.append(n)
        else:
            composites.append(n)

    for n in composites:
        if all((n - p) // 2 not in squares for p in primes):
            return n


print(p46())
