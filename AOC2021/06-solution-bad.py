import numpy as np

fish = np.loadtxt("input/06", delimiter=",", dtype=int)
baby = np.full((1,1), 8)

day = 0

while day < 80:
    for i in np.ndenumerate(fish):
        #print(i[0][0], "    ", i[1])
        if i[1] > 0:
            fish[i[0][0]] -= 1
        elif i[1] == 0:
            fish[i[0][0]] = 6
            fish = np.append(fish, baby)
    day += 1

print("part1:", len(fish))


while day < 256:
    for i in np.ndenumerate(fish):
        #print(i[0][0], "    ", i[1])
        if i[1] > 0:
            fish[i[0][0]] -= 1
        elif i[1] == 0:
            fish[i[0][0]] = 6
            fish = np.append(fish, baby)
    day += 1

print("part2:", len(fish))

