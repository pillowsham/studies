def is_even(n):
    return n % 2 == 0


def has_even_digit(n):
    return any(is_even(i) for i in map(int, str(n)))


def gen_primes(n):
    max_n = (n - 3) // 2 + 1
    sieve = [True] * max_n

    i = 0
    while (2 * i + 3) ** 2 <= n:
        if sieve[i]:
            for j in range(2 * i * i + 6 * i + 3, max_n, 2 * i + 3):
                sieve[j] = False
        i += 1

    return [2] + [2 * i + 3 for i in range(max_n) if sieve[i] and not has_even_digit(2 * i + 3)]


def p35(n):
    primes = gen_primes(n)

    def is_circular(x):
        s = str(x)
        return all(int(s[i:] + s[:i]) in primes for i in range(1, len(s)))

    return len(list(filter(is_circular, primes)))


assert p35(100) == 13
print(p35(1000000))
