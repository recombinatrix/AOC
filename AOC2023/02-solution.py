#!/usr/bin/env python

import numpy as np
tests = {
    'red' : 12,
    'green' : 13,
    'blue' : 14,
}
powers = 0
games = 0
with open("input/02") as f:
    for line in f:
        line=line.strip()
        game = int("".join([(i) for i in line.split(':')[0] if i.isdigit()]))
        this = [i.strip().split(",") for i in line.split(':')[1].split(';')]
        valid = True
        min = {'red':0,'blue':0,'green':0}
        for i in this:
            for pull in i:                
                count,colour = pull.strip().split(" ")
                min[colour] = max([int(count),min[colour]])
                if int(count) > tests[colour]:
                    valid = False
        if valid:games += game
        power = min['red'] * min['blue'] * min['green']
        powers += power
print(games)
print(powers)

# did this in the airport while waiting for a flight home