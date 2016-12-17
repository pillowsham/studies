from itertools import combinations

SIZE = 10000

sieve = [True] * SIZE
for i in range(4, SIZE, 2):
  sieve[i] = False

for i in range(3, SIZE, 2):
  if sieve[i]:
    for j in range(i*i, SIZE, 2*i):
      sieve[j] = False

counts = {}
for i in range(1000, 10000):
  if sieve[i]:
    digits = str(sorted(str(i)))
    counts.setdefault(digits, []).append(i)

for v in counts.values():
  if len(v) >= 3:
    for c in combinations(v, 3):
      if abs(c[0] - c[1]) == abs(c[1] - c[2]):
        print(c, str(c[0]) + str(c[1]) + str(c[2]))
