# -*- coding: utf-8 -*-

SIZE = 200

arr = [1] + [0]*SIZE

for c in [1, 2, 5, 10, 20, 50, 100, 200]:
    for i in range(c, SIZE+1):
        arr[i] += arr[i-c]

print(arr[-1])