from functools import lru_cache

digits = [i for i in range(1, 10)]


@lru_cache(maxsize=None)
def is_prime(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if x % 2 == 0:
        return False

    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def is_truncatable_prime(n):
    n1 = n2 = n

    while n1 > 0:
        if not is_prime(n1):
            return False
        s = str(n1)
        n1 = int(s[1:]) if len(s) > 1 else 0

    while n2 > 0:
        if not is_prime(n2):
            return False
        n2 //= 10

    return True


def next_value(n):
    for f in digits:
        m = 10 * n + f
        if is_prime(m):
            if is_truncatable_prime(m):
                yield m

            for j in next_value(m):
                yield j
    raise StopIteration


truncatable_primes = set(j for i in digits for j in next_value(i))
assert len(truncatable_primes) == 11
print(sum(truncatable_primes))
