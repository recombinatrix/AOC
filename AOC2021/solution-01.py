import numpy as np

def ImportData(filename):
    # fucntion to import data from a text file
    data = np.loadtxt(filename)
    return data

#input the problem data as sonar
sonar = ImportData("input/01")

# for part 1

# turn sonar into a 2d array. 
# Column 0 will be all the sonar values in order, starting from the 1st value (ie skip the 0th)
# Column 1 will  be all the sonar values in order, starting from the 0th value and skipping the final value
# Then glue them together as a 2d array with each row being [   sonar[i]  ,  sonar[i-1]   ]

a = np.column_stack((sonar[1:], sonar[:-1]))

# make a variable to count how many times depth increases
 
count = 0

#iterate over the elements of a.  if a sonar element x[0] is greater than the preceeding sonar element x[1], increase the count by one 
for x in a:
    if x[0] > x[1]:
        count += 1    

# return the answer to part 1
print(count)

# part 2

# get the length of sonar
n = sonar.shape[0]

x = 0
count = 0
while x < (n - 3): 
    sum1st = sonar[x] + sonar[x+1] + sonar[x+2]
    sum2nd = sonar[x+1] + sonar[x+2] + sonar[x+3]
    if sum1st < sum2nd:
        count += 1
    x += 1

# return the answer to part 2

print(count)