from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)

for line in open('input/07'):
    #print (line)
    #print()
    if line.split()[0] == '$':
        if line.split()[1] == 'ls':
            pass
        elif line.split()[1] == 'cd':
            loc = line.split()[2]
            if loc == "/":
                curr = ['/']
            elif loc == "..":
                curr.pop()
            else:
                curr.append(loc + '/')
    elif line [0:3] == 'dir':
        pass
    elif line [0] in '0123456789':
        size = int(line.split()[0])
        for p in accumulate(curr):
            dirs[p] += int(size)   # i am concerned what would happen if the puzzle input used ls in the same directry twice
                                   # i think in such a case it would double count those files?
                                   # it doesn't seem to happen but I distrust it
    #print(curr)
    #for k,v in dirs.items():
    #    print(k,v)
    
here = [ v for k,v in dirs.items() if v <= 100000]
print(sum(here))
disk = 70000000
free = disk - dirs['/']
req = 30000000 - free

kill = [v for k,v in dirs.items() if v >= req]
print(min(kill))