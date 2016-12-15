from itertools import permutations

r = 0
for p in permutations("0123456789", 10):
    p = ''.join(p)
    if int(p[1:4]) % 2: continue
    if int(p[2:5]) % 3: continue
    if int(p[3:6]) % 5: continue
    if int(p[4:7]) % 7: continue
    if int(p[5:8]) % 11: continue
    if int(p[6:9]) % 13: continue
    if int(p[7:10]) % 17: continue
    r += int(p)

print(r)
