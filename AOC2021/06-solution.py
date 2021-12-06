import numpy as np
data = np.loadtxt("input/06", delimiter=",", dtype=int)
fish = np.zeros((9,1), dtype=int)

def fishbreeder(arr, days):
    for day in range(days):
        new = np.zeros((9,1), dtype=int)
        for i in np.ndenumerate(arr):
            if i[0][0] == 0:
                new[8,0] = i[1]
                new[6,0] = i[1]
            else:
                new[i[0][0]-1,0] += i[1]
        arr = new
    return(np.sum(arr[:,0]))

for i in range(9): 
    count = np.count_nonzero(data == i)
    total -= count 
    fish[i,0] = count

print(fishbreeder(fish,80))
print(fishbreeder(fish,256))