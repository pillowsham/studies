from itertools import accumulate
from bisect import bisect


def gen_primes(n):
  sieve = [True]*n
  for i in range(n):
    if sieve[i]:
      for j in range(2*i*i + 6*i + 3, n, 2*i + 3):
        sieve[j] = False
  return [0, 2] + [2*i+3 for i in range(n) if sieve[i]]


PRESEED_SIZE = 1000000
PRESEED_PRIMES = gen_primes(PRESEED_SIZE // 2)
PRESEED_CUM_SUMS = list(accumulate(PRESEED_PRIMES))


# returns (prime_count, prime)
def p50(pmax):
  n = bisect(PRESEED_PRIMES, pmax)

  primes = PRESEED_PRIMES[:n]
  cum_sums = PRESEED_CUM_SUMS[:n]

  d_max, v_max = 1, 0

  for i in range(n - 1):
    for j in range(i + d_max + 1, n):
      ps = cum_sums[j] - cum_sums[i]

      if ps > pmax:
        break
      elif ps in primes:
        d_max = j - i
        v_max = ps

  return (d_max, v_max)


assert p50(10 ** 2) == (6, 41)
assert p50(10 ** 3) == (21, 953)
print(p50(10 ** 6))

