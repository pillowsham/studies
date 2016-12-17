SIZE = 1000000

sieve = [True] * SIZE
factors = [0] * SIZE

factors[2] = 1
for i in range(4, SIZE, 2):
  factors[i] += 1

for i in range(3, SIZE, 2):
  if sieve[i]:
    factors[i] += 1
    for j in range(2*i, SIZE, i):
      factors[j] += 1
      sieve[j] = False

def p47(n):
  for i in range(SIZE-n):
    if all(factors[i+j] == n for j in range(n)):
      return i

  return None

print(p47(2))
print(p47(3))
print(p47(4))
