import numpy as np

b = np.genfromtxt('input/08',dtype=str)
a = np.array([list(x) for x in b]).astype(int)
a

def viewdist(a,t):
    dist = 0
    for i in a:
        dist +=1 
        if i >= t:
            break
    return(dist)

xmin = 0
xmax = a.shape[0]-1
ymin = 0
ymax = a.shape[1]-1

viewmax = 0
count = 0
for idt, t in np.ndenumerate(a):
    #print(idx, x)
    x = idt[0]
    y = idt[1]

    x1 = a[x,:y]
    x1v = np.flip(x1)
    x1vd = viewdist(x1v,t)
    x2 = a[x,y+1:]
    x2vd = viewdist(x2,t)
    y1 = a[:x,y]
    y1v = np.flip(y1)
    y1vd = viewdist(y1v,t)
    y2 = a[x+1:,y]
    y2vd = viewdist(y2,t)

    scenic = x1vd * x2vd * y1vd * y2vd
    if scenic > viewmax:
        viewmax = scenic
    if (x in [xmin,xmax] or y in [ymin,ymax]): # is it on an edge?
        count += 1 # it's a pain to use the visibility checker on the edges
    else:
        if t > min([x1.max(),x2.max(),y1.max(),y2.max()]): # visibility checker
            count += 1        



    # print(a)
    # print()
    # print (idt,t,x1,x1vd,x2,x2vd)
    # print (idt,t,y1,y1vd,y2,y2vd)
    # print('scenic',scenic)
    # print()
    

print (count)
print(viewmax)

