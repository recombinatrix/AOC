
import numpy as np
data = np.loadtxt("input/06", delimiter=",", dtype=int)
fish = np.zeros((9,1), dtype=int)


def fishbreeder(arr, days):
    """Calculate the number of lapfish from a starting population after a certain number of days. 
    Takes (arr, days). 
    arr is a (9,1) array where arr[n] is the number of fish at with n days left before breeding 
    days is the number of days to breed fish 
    Returns a tuple with two elements
    fishfinder[0] is the number of fish after the final day
    fishfinder[1] containing the number of fish at the start of each day 
    because the value of fishfinder[1] is the start of the day before breeding, the size of popgraph is days + 1"""
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
    return(np.sum(arr[:,0]), popgraph)


for i in range(9): 
    count = np.count_nonzero(data == i)
    fish[i,0] = count

print(fishbreeder(fish,80)[0])
print(fishbreeder(fish,256)[0])

#alternate method based on exponents
# print("part2:", int(1.11622269641992 ** 256))
