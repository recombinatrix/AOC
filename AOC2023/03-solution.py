#!/usr/bin/env python

# don't expect much; your girl has covid

import math as m,re

fpath='input/03'

a = list(open(fpath))
limit = len(str(a[0]).strip())

count = 0

for i, row in enumerate(a):
    for n in re.finditer(r'\d+', row):
        #print(i,n)

        if int(n.start()) > 0: xmin = n.start()-1
        else: xmin=0

        if int(n.end()) < limit: xmax = n.end()+1 
        else: xmax = limit

        checker=row[xmin:xmax]

        if i >0:

            checker += a[i-1][xmin:xmax]

        if i < len(a)-1:

            checker += a[i+1][xmin:xmax]

        this = n.group(0)

        if bool([q for q in checker if q not in '0123456789.']): count += int(n.group(0))


print(count)
    

# this is a really clumsy way to do it.  
# for each instance of a number, I'm extracting the number plus the surrounding characters as a string,
# then testing for special characters inside that string.  this means I need to explicitly handle edge cases
# i saw a much more elegant solution that works as follows:
# first, extract the coordinates of every symbol and save them to a dictionary
# second, cycle through and find the numbers inside theinput
# for every number, get the coordinate range for it, and it's adjacent digits.  
# this is only a range of numbers, so it can include coordinates  that aren't present in the input data (eg:  x = negative 1)
# check whether any of the symbols fall in that coordinate range.  if yes, keep the number for scoring.
   
# and then we get to part two and realise we have done it *wrong*
# should have been iterating over the symbols from the beginning.

gears = {(r,c): [] for r in range(len(a)) for c in range(limit) if a[r][c] in '*'}
# make a dictionary of all gears

# look for numbers
for i, row in enumerate(a):
    for n in re.finditer(r'\d+', row):
        zone = {(r,c) for c in range(n.start()-1,n.end()+1) for r in (i-1,i,i+1)}   #define the surrounding area as a dictionary of coordinates that fall within the surrounding characters
        for gear in zone & gears.keys(): # which coordinates are in the zone and are also gears?
            gears[gear].append(int( n.group())) # append the number to the adjacent gear

print(sum([m.prod(g) for g in gears.values() if len(g) == 2])) # use list comprehension to extract the gears with two numbers, get the gear ratios for those gears, return the sum of all of these)