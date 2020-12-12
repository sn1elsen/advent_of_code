#!/usr/bin/python

import re
import sys

def test_height(v):
    res = re.match(r'([0-9]{2,3})(cm|in)', v)
    retval = False
    if res:
        (val, type) = res.groups()
        if type == 'cm' and int(val) >= 150 and int(val) <= 193:
            retval = True
        elif type == 'in' and int(val) >= 59 and int(val) <= 76:
            retval = True
    return retval

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
passports = []
valid = 0

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
        tests = [test(passport[field]) for field, test in FIELDS.items()]
        if all(tests):
            valid += 1

print("%s" % valid)
