#!/usr/bin/python

import re
import sys

data = []
for line in sys.stdin:
    data.append(line.rstrip())

valid = 0
for line in data:
    (pos1, pos2, char, passwd) = re.split(r'[-: ]+', line)
    count = passwd.count(char)
    if count >= int(pos1) and count <= int(pos2):
        valid += 1

print("valid %s" % valid)

sys.exit(0)
