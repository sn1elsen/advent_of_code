#!/usr/bin/python

import re
import sys

data = []

for line in sys.stdin:
    data.append(line.rstrip())

# 15-16 g: sggggggggqgclgggmggw

valid = 0
for i in data:
    (r1, r2, char, passwd) = re.match('^([0-9]{1,})\-([0-9]{1,})\s+([a-z]):\s+(.*)$', i).groups()
    count = passwd.count(char)
    if count >= int(r1) and count <= int(r2):
        valid += 1

print("valid %s" % valid)

sys.exit(0)
