#!/usr/bin/python

import sys

answers = {}


def process(group, item):

    for char in item:
        if not char in answers[group]['chars']:
            answers[group]['chars'][char] = 1
        else:
            answers[group]['chars'][char] += 1


group = 0
item = ''

for line in sys.stdin:
    line2 = line.rstrip()
    if line2:
        if not group in answers:
            answers[group] = {}
            answers[group]['chars'] = {}
            answers[group]['count'] = 1
        else:
            answers[group]['count'] += 1
        item += line2
    else:
        process(group, item)
        group += 1
        item = ''

process(group, item)

group = 0
total = 0

for group in answers:
    for char in answers[group]['chars']:
        if answers[group]['count'] == answers[group]['chars'][char]:
            total += 1

print(total)
