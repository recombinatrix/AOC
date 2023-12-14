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