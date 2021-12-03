import numpy as np
from scipy import stats

# import data

diag = np.genfromtxt('input/03', delimiter = 1).astype(int) # make a numpy array where each line is a row, and each character is a single entry

# for part 1, we need to find the most common digit in each column, and the least common digit
# there are only two digits; if the most common is one, the least common is 0
# so we only need to solve the problem once and then flip the bits

def invert(arr):
    # invert the values of an array of single binary digits 
    inv = [1 - a for a in arr]
    return np.array(inv)

def bin2int(arr):
    #turn an array of binary digits into an int
    data = int(sum([j*(2**i) for i,j in list(enumerate(reversed(arr)))])) # reverses the order of bits, ennumerates them so they are a tuple of shape (index, bit)
    return data

g = (stats.mode(diag))[0][0] # calculate gamma
e = invert(g) # calulate epsilon
print("part 1: " + str(bin2int(g)*bin2int(e)))

# for part two it is similar, but the size of the data set shrinks each time
# because the size of the data set changes each time, we can't just flip the bits

# stats.mode will return the smallest mode if there are two equally present values, which would be zero
# for the oxygen output, we want to keep the largest of the modes
# if we invert diag, run the filter on it, and then swap it back stats.mode will return the largest mode

def run_filter(arr,str):
    x = 0
    arrf = arr
    while x < arr.shape[1]: # run filter_loop over each column, using the filtered input of column i for column i+1
        filterx = filter_loop(arrf,x,str) # I could probably just insert the filter loop into the function but this is easier to read
        arrf = filterx 
        x += 1
    return arrf[0]

def filter_loop(arr, col,str):
    if (np.shape(arr)[0] == 1): # stop once we only have one value; otherwise stats.mode gets mad
        return arr
    else:
        inv = invert(arr) # invert array so stats.mode works as intended
        filter = np.empty([0,12])
        if str=="ox":
            value = stats.mode(inv[:,col])[0][0] #calculate mode of column, keeping smallest mode (which is largest because we inverted)
        if str=="scrub":
            value = 1 - stats.mode(inv[:,col])[0][0] #calculate mode of column, keeping smallest mode (which is largest because we inverted), then reverse the bit so we keep the anti-mode
        for data in inv:
            if data[col] == value:
                filter = np.row_stack((filter,data))
        return invert(filter)

print ("part 2: " + str(bin2int(run_filter(diag,"ox"))*bin2int(run_filter(diag,"scrub"))))
