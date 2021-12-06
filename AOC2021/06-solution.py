
import numpy as np
data = np.loadtxt("input/06", delimiter=",", dtype=int)
fish = np.zeros((9,1), dtype=int)

def fishbreeder(arr, days):
    popgraph = np.zeros((days,2), dtype=int)
    for day in range(days):
        popgraph[day,0] = day
        popgraph[day,1] = np.sum(arr[:,0])
        new = np.zeros((9,1), dtype=int)
        for i in np.ndenumerate(arr):
            if i[0][0] == 0:
                new[8,0] = i[1]
                new[6,0] = i[1]
            else:
                new[i[0][0]-1,0] += i[1]
        arr = new
    # returns a tuple. [0] is n(fish) on the final day, [1] is a 2d array of days versus n(fish), for graphing
    return(np.sum(arr[:,0]), popgraph)

for i in range(9): 
    count = np.count_nonzero(data == i)
    fish[i,0] = count

day80 = fishbreeder(fish,80)
print(day80[0])
day256 = fishbreeder(fish,256)
print(day256[0])

#alternate method based on exponents
# print("part2:", int(1.11622269641992 ** 256))

