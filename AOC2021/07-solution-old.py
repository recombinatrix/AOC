import numpy as np
data = crabs = np.loadtxt("input/07", delimiter=",", dtype=int)
uses,cuses = [], []
for i in range(np.min(crabs),np.max(crabs)+1,1): #check all positions from first crab to last crab
    use = cuse =  0
    #print("checking position",i,"from range",np.min(crabs),"to",np.max(crabs)+1)
    for j in crabs:
        fuel = abs(j - i)
        use += fuel
        cuse += int((fuel * (fuel + 1))/2)
        #print("crab position:" ,j,"to position:", i, "fuel cost:", abs(i-j), "total fuel cost for position", i, ":", use) 
    uses.append(use)
    cuses.append(cuse)
print(min(uses))
print(min(cuses))
