def to_number(w):
    return sum(ord(c) - 64 for c in w)


words = sorted(map(to_number, list(name[1:-1] for name in open("p042_words.txt", 'r').read().split(','))))
triangles = {i * (i + 1) // 2 for i in range(1, 20)}

print(len(list(filter(lambda i: i in triangles, words))))
