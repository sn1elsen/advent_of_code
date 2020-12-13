#!/usr/bin/python

import sys

def get_seat(region):

    rmin, rmax = 0, 127
    smin, smax = 0, 7

    for half in [char for char in region]:
        if half == 'F':
            rmax = rmax - ((rmax-rmin)/2) - 1
            rhalf = half
        elif half == 'B':
            rmin = rmin + ((rmax-rmin)/2) + 1
            rhalf = half
        elif half == 'L':
            smax = smax - ((smax-smin)/2) - 1
            shalf = half
        elif half == 'R':
            smin = smin + ((smax-smin)/2) + 1
            shalf = half

    row = rmin if rhalf == 'F' else rmax
    seat = smin if shalf == 'L' else smax
    seat_id = (row * 8) + seat

    return seat_id


seat_ids = []
for line in sys.stdin:
    line.rstrip()
    seat_ids.append(get_seat(line))

seat_ids.sort()

seat_id = sum(xrange(seat_ids[0], seat_ids[-1]+1)) - sum(seat_ids)

print("my seat id %s" % seat_id)
