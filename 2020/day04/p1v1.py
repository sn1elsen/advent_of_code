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

item = ''
valid = 0
passports = []

for line in sys.stdin:
    line2 = line.rstrip()
    if line2:
        if item:
            item += ' '
        item += line2
    else:
        attrs = item.split()
        passport = {}
        for attr in attrs:
            (name, value) = attr.split(':')
            passport[name] = value
        item = ''
        passports.append(passport)

passports.append(passport)

for passport in passports:
    if all(req in passport.keys() for req in FIELDS):
        valid += 1

print("%s" % valid)
