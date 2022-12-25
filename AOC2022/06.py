#!/usr/bin/env python 

# this one is really simple, just look for sets of four characters 

with open("input/06") as f:
    raw = list(f.readlines()[0].strip())
i = 0
while i < len(raw):

    if len(set(raw[i:i+4])) == len(raw[i:i+4]): # if there are 4 unique characters, length of set is the same as the length of the list
        print (i + 4)
        break
    i +=1

i = 0
while i < len(raw):
    if len(set(raw[i:i+14])) == len(raw[i:i+14]):
        print (i + 14)

        break
    i +=1
