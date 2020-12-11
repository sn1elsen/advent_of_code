#!/usr/bin/python

import re
import sys

data = []

for line in sys.stdin:
    data.append(line.rstrip())

# 15-16 g: sggggggggqgclgggmggw

valid = 0
for i in data:
    pieces = re.match('^([0-9]{1,})\-([0-9]{1,})\s+([a-z]):\s+(.*)$', i).groups()
    count = pieces[3].count(pieces[2])
    if count >= int(pieces[0]) and count <= int(pieces[1]):
        valid += 1

print("valid %s" % valid)

sys.exit(0)
