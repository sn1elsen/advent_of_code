#!/usr/bin/python

import re
import sys


def has_char(passwd, char, pos1, pos2):
    found = 0
    for i, c in enumerate(passwd):
        if c == char and i == pos1:
            found += 1
        elif c == char and i == pos2:
            found += 1
    if found == 1:
        return True
    else:
        return False


data = []
for line in sys.stdin:
    data.append(line.rstrip())

valid = 0
for line in data:
    (pos1, pos2, char, passwd) = re.split(r'[-: ]+', line)
    if has_char(passwd, char, int(pos1)-1, int(pos2)-1):
        valid += 1

print("valid %s" % valid)

sys.exit(0)
