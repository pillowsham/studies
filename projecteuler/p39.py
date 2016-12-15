counts = [0] * 1001
squares = {i * i: i for i in range(1001)}

for a in range(1, 1000):
    for b in range(1, 1000):
        c2 = a * a + b * b
        if c2 in squares:
            c = squares[c2]
            p = a + b + c
            if p <= 1000:
                counts[p] += 1
            else:
                break

print(counts.index(max(counts)))
