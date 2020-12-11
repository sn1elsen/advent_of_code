#!/usr/bin/python

import itertools
import sys

data = []

for line in sys.stdin:
    data.append(int(line.rstrip()))

for i, j in itertools.product(data, data):
    if (i + j) == 2020:
        print("answer is %s, %s, %s" % (i, j, i * j))
        break

sys.exit(0)
