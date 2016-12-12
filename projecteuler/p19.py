# -*- coding: utf-8 -*-

from datetime import date

def sequence():
    x = date(1901, 1, 1)
    while x <= date(2000, 12, 31):
        yield x
        if x.month < 12:
            x = x.replace(month=x.month + 1)
        else:
            x = x.replace(year=x.year + 1, month=1)

print(len(list(filter(lambda d: d.weekday() == 6, sequence()))))