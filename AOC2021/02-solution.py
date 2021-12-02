import numpy as np

#generate three scalars from the input file

up = sum(np.loadtxt("input/02", comments=["do", "fo"],dtype=str)[:,1].astype(np.int8)) 
down = sum(np.loadtxt("input/02", comments=["up", "fo"],dtype=str)[:,1].astype(np.int8))
forward = sum(np.loadtxt("input/02", comments=["up", "do"],dtype=str)[:,1].astype(np.int8)) #comment needs to be "do" not "d" because there is a d in forward
print("part one: " + str(forward * (down - up)))

# oh well, this won't work at all for part 2

nav = np.loadtxt("input/02",dtype=str)
nav[:,1].astype(np.int8)

pos = [0, 0]
aim = 0

for (a, b) in nav:
    if a == "up":
        aim -= int(b)
    if a == "down":
        aim += int(b)
    if a == "forward":
        pos[0] += int(b)
        pos[1] += (int(b) * aim)

print("part two: " + str(pos[0] * pos[1]))

# going to see if I can come up with a more elegant solution to this