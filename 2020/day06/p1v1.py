#!/usr/bin/python

import sys

answers = {}


def process(group, item):

    if not group in answers:
        answers[group] = {}
    for char in item:
        answers[group][char] = 1


group = 0
item = ''

for line in sys.stdin:
    line2 = line.rstrip()
    if line2:
        item += line2
    else:
        process(group, item)
        group += 1
        item = ''

process(group, item)

group = 0
total = 0
for group in answers:
    for char in answers[group]:
        total += 1

print(total)
