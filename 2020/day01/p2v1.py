#!/usr/bin/python

import itertools
import sys

data = []

for line in sys.stdin:
    data.append(int(line.rstrip()))

for i, j, k in itertools.product(data, data, data):
    if (i + j + k) == 2020:
        print("answer is %s, %s, %s, %s" % (i, j, k, i * j * k))
        break

sys.exit(0)
