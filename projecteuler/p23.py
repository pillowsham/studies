# -*- coding: utf-8 -*-
from itertools import combinations_with_replacement

N_MAX = 23000

numbers = [0, 0] + [1]*(N_MAX-1)

for i in range(2, N_MAX+1):
    for j in range(2*i, N_MAX+1, i):
        numbers[j] += i

abundant_numbers = set(i for i,s in enumerate(numbers) if s > i)
possible_sums = set(map(sum, combinations_with_replacement(abundant_numbers, 2)))

print(sum(i for i in range(1, N_MAX) if i not in possible_sums))