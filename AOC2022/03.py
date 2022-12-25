#!/usr/bin/env python 


import string # lets use string methods to get the alphabet!
import numpy as np

d = {} # make a dictionary of values for each letter
for k in list(string.ascii_lowercase):
    d[k] = ord(k) - 96 # ord gets ascii character order, "a" is 97
for k in list(string.ascii_uppercase):
    d[k] = ord(k) - 38 # "a" is 65, want A to be 27, so ord(k) - 64 + 26

# lower case numbers, ord(a) = 97 - 96
score = 0
with open("input/03") as f:
    raw = np.array(f.readlines())

for e in raw:
        c1, c2 = (e[:int(len(e)/2)]) , (e[int(len(e)/2):]) # split each line in half
        bad = d["".join(set(c1).intersection(c2))] #use sets to find the item present in both elements, get it's score from d
        score += bad

print(score) #part1
raw
teams = np.reshape(raw,(-1,3)) # turn it into a n by 3 array

badges=0
for i in range(teams.shape[0]): #itterate over the rows
    badges += d["".join(list(set(teams[i,0]).intersection(teams[i,1],teams[i,2],string.ascii_letters)))] # 
print(badges)