
import numpy as np
data = np.loadtxt("input/06", delimiter=",", dtype=int)
fish = np.zeros((9,1), dtype=int)


def fishbreeder(arr, days):
    popgraph = np.zeros((days+1,1), dtype=int) #to store number of fish at end of each day
    for day in range(days):
        if (day) == 0:
            popgraph[day,0] = np.sum(arr[:,0])
        new = np.zeros((9,1), dtype=int)
        for i in np.ndenumerate(arr):
            if i[0][0] == 0:
                new[8,0] = i[1]
                new[6,0] = i[1]
            else:
                new[i[0][0]-1,0] += i[1]
        arr = new
        popgraph[day+1,0] = np.sum(arr[:,0])
    # tuple[0] is n(fish) on the final day
    # tuple[1] contains a 1d array of n(fish) at the start of day n
    # because the value is the start of the day before breeding, the size of popgraph is days + 1
    return(np.sum(arr[:,0]), popgraph)


for i in range(9): 
    count = np.count_nonzero(data == i)
    fish[i,0] = count

print(fishbreeder(fish,80)[0])
print(fishbreeder(fish,256)[0])

#alternate method based on exponents
# print("part2:", int(1.11622269641992 ** 256))
