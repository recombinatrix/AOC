#!/usr/bin/env python 

import pandas as pd
import math

with open("input/05") as f:
    raw = f.readlines()


# extract the starting positions
start = ([ x for x in raw if "[" in x  ]) 

#convert starting positions to a set of nine strings, with topmost element first

cols = math.ceil(len(start[-1])/4) # get length of final row of the start break into columns

arr = [[]] # initial zeroth row for easy indexing, so sloppy
j = 1
for i in range(0,cols):
    new = []
    for r in start:
        new.append(r[j:j+1])
    arr.append("".join(new).strip())
    j += 4
arr


# extract the moves
moves = ([ list(map(int,(x.strip().split(" ")[1::2]))) for x in raw if "move" in x  ])

i = 1
piles=arr.copy()
piles2=arr.copy()
for move in moves:
    

    piles[move[2]] = piles[move[1]][:move[0]][::-1] + piles[move[2]]
    piles[move[1]] = piles[move[1]][move[0]:]
    piles2[move[2]] = piles2[move[1]][:move[0]] + piles2[move[2]]
    piles2[move[1]] = piles2[move[1]][move[0]:]
    i+=1

print("".join([x[0] for x in piles[1:]]))
print("".join([x[0] for x in piles2[1:]]))
