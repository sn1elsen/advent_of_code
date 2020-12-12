#!/usr/bin/python

import sys

data = []
for line in sys.stdin:
    data.append(line.rstrip())

right = 3
down = 1
trees = 0
col = 0

for line in data[down::down]: # start on row 1, step 1 throughh array
    col += right
    if line[col % len(line)] == '#':
        trees += 1

print("trees encountered %s" % tree)
