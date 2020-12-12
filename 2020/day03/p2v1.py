#!/usr/bin/python

import sys

data = []
for line in sys.stdin:
    data.append(line.rstrip())

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

answer = 1

for pair in slopes:
    col, trees = 0, 0
    for line in data[pair[1]::pair[1]]:
        col += pair[0]
        if line[col % len(line)] == '#':
            trees += 1
    answer = answer * trees

print("trees encountered %s" % answer)
