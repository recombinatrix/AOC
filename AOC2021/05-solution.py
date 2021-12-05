import numpy as np
vents = np.fromregex('input/05', r'[0-9]+', [("num", np.int16)]).reshape(-1,2,2)['num']
vmap = np.zeros((np.max(vents),np.max(vents)), dtype=int) # make map

# part 1: label orthoganal vents
#in retrospect this would've been easier if I just calculated to coordinates and iterated over them

hvents = np.array([v for v in vents if np.equal(v[0,0] , v[1,0])]) #horizontal vents
vvents = np.array([v for v in vents if np.equal(v[0,1] , v[1,1])]) #vertical vents

for vent in hvents:
    print("hvents", vent)
    for i in np.ndenumerate(vmap[vent[0,0]]):
        if min(vent[:,1]) <= i[0] <= max(vent[:,1]): #test y coord
            vmap[ vent[0,0], (i[0]) ] += 1

for vent in vvents:
    print("vvents",vent)
    for i in np.ndenumerate(vmap[:,vent[1,1]]):
        if min(vent[:,0])  <= i[0] <= max(vent[:,0]): # test x coord
            vmap[ i[0], vent[1,1] ] += 1

danger = len([a for a in vmap.flatten() if (a > 1)]) # how many sites in vmap are > 1
print("part1:", danger)

# part two: diagonal vents
# for diagonals I made a list of all coordinates in the diagonal

def diagtest(v):
    if not (np.equal(v[0,0] , v[1,0]) or np.equal(v[0,1] , v[1,1])): 
        return True

dvents = np.array([v for v in vents if diagtest(v)])
dcoords = [ ]

for vent in dvents:
    vlen = (np.max(vent[:,0]) - np.min(vent[:,0])) # get length
    i = 0
    #figure out which way the diagonal goes
    if (vent[0,0] < vent[1,0] and vent[0,1] < vent [1,1]) or (vent[0,0] > vent[1,0] and vent[0,1] > vent [1,1]):
        while i < vlen + 1:
            coord = ((np.min(vent[:,0]) + i) , (np.min(vent[:,1]) + i))
            dcoords.append(coord)
            i += 1
    else:
        while i < vlen + 1:
            coord = (np.min(vent[:,0]) + i, np.max(vent[:,1]) - i)
            dcoords.append(coord)
            i += 1

for point in dcoords:  
    vmap[ point[0], point[1] ] += 1

danger = len([a for a in vmap.flatten() if (a > 1)]) # how many sites in vmap are > 1
print("part2", danger)

# for plotting it

import matplotlib
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (32 , 32)

fig, ax = plt.subplots()
im = ax.imshow(vmap.T)
im.figure.savefig('05-seafloor.png')