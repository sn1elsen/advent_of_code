#!/usr/bin/python

import sys

FIELDS = {
        'byr': lambda v: 1920 <= int(v) <= 2002,
        'iyr': lambda v: 2010 <= int(v) <= 2020,
        'eyr': lambda v: 2020 <= int(v) <= 2030,
        'hgt': lambda v: v and test_height(v),
        'hcl': lambda v: re.match(r'#[a-f0-9]{6}$', v),
        'ecl': lambda v: v in 'amb blu brn gry grn hzl oth'.split(' '),
        'pid': lambda v: re.match(r'\d{9}$', v),
        }

data = ''
for line in sys.stdin:
    data += line

valid = 0
for lines in data.split('\n\n'):
    passport = {}
    for text in lines.split():
        key, value = text.split(':')
        passport[key] = value
    if all(req in passport.keys() for req in FIELDS):
        valid += 1

print(valid)
