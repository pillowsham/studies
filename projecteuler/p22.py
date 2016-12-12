# -*- coding: utf-8 -*-
from itertools import starmap


def estimate(i, name):
    baseOrd = ord('A') - 1
    return (i+1) * sum(ord(i) - baseOrd for i in name)


names = list(name[1:-1] for name in open("p022_names.txt", 'r').read().split(','))
names = sorted(names)

print(sum(starmap(estimate, enumerate(names))))