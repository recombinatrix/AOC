d = {}

mode=False
t = 0
modes = {}


with open("input/05") as f:
    for line in f:

        if ':' in line:

            if line.split(':')[0]=='seeds':
                seeds = [int(x) for x in line.strip().split(':')[1].split()]


            elif line.split(':')[0].split()[1]=='map':
                mode = line.split(':')[0].split()[0]
                d[mode]={}
                modes[t]=mode
                t+=1
                #print(mode)

        else:
            if len(line.strip().split()) == 3:
                here = [int(x) for x in line.strip().split()]
                dest = here[0]
                source = here[1]
                run = here[2]
                diff = dest - source
                smax = source + run
                d[mode][(source,smax)]=diff

plots = []

for s in seeds:
    for i in range(t):
        change = False
        for k,v in d[modes[i]].items():
            if s in range(k[0],k[1]) and not change:
                s = s + v   
                change = True
    plots.append(s)
print(min(plots))


# bigseeds = list(zip( seeds[::2], seeds[1::2]))
# print(bigseeds)
# bigplots=[]
# for r in bigseeds:
#     print(r)
#     for s in range (r[0],r[0]+r[1]):
#         #print('in:',s)
#         for i in range(t):
#             change = False
#             for k,v in d[modes[i]].items():
#                 if s in range(k[0],k[1]) and not change:
#                     s = s + v   
#                     change = True
#                     #print(mode,s)
#         #print('out:',s)
#         bigplots.append(s)
#         #print()
#         bigplots = [min(bigplots)]
# print(min(bigplots))

# ah
# numbers go up
# lets do this more sensibly


# i can see what I need to do (construct ranges in each space, find the edges of those ranges, so I can find the minima at each level )
# but my covid addled brain is struggling with actually doing that
# i need a whiteboard to diagram it
# i think the best answer is probably to start by looking at the ranges in locationspace, based on the location mapping 
# then step backwards and generate the ranges in humidity space, based on the interactions between the humidity mapping and the loaction mapping
# and work backwards from there till I get the ranges in soilspace
# then, propagate forward from seedspace, getting the piecewise seedspace ranges based on the seven piecewise mappings
# and map the start of each seedspace range to the corresponding point in locationspace, then take the minima of those

# working backwards seems wise because it lets me find the segments with identity mappings

# also I wish I had used a dictionary corresponding to the eight spaces, rather than a dictionary of the seven mappings
# i'll rework it later