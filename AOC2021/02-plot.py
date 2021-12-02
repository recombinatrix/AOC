import numpy as np
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.style.use('seaborn-dark-palette')

def ImportData(filename):
    data = np.loadtxt(filename, comments=["#", "@"])
    return data

#input the day 01 data as sonar
sonar = ImportData("input/01")

# input the day 02 data as poscalc
up = sum(np.loadtxt("input/02", comments=["do", "fo"],dtype=str)[:,1].astype(np.int8))
down = sum(np.loadtxt("input/02", comments=["up", "fo"],dtype=str)[:,1].astype(np.int8))
forward = sum(np.loadtxt("input/02", comments=["up", "do"],dtype=str)[:,1].astype(np.int8))
poscalc = (forward , (down - up))


# calulate trajectory


nav = np.loadtxt("input/02",dtype=str)
nav[:,1].astype(np.int8)

pos = [0,0]
traj =  np.zeros(shape=(1,2)).astype(np.int8)
aim = 0

for (a, b) in nav:
    if a == "up":
        aim -= int(b)
    if a == "down":
        aim += int(b)
    if a == "forward":
        pos[0] += int(b)
        pos[1] += (int(b) * aim)
        traj = np.row_stack((traj, pos))

plt.rcParams["figure.figsize"] = (16 , 12)
plt.rcParams['axes.facecolor']='#b5a299'

ax1 = plt.subplot(111)
ax1.set_title("Depth")
ax1.plot(range(0, sonar.shape[0]), sonar[:], label="Depth") # range arbitrarily numbers x from 0 to the size of the 1D sonar array
ax1.set_xlabel("Across")
ax1.set_ylabel("Depth")
ax1.set_xlim([0, 2000])
ax1.set_ylim([5500, 0])
ax1.plot(poscalc[0], poscalc[1], marker="x", markeredgecolor="red", markerfacecolor="red", label="Calculated position")
ax1.plot(traj[:,0], traj[:,1], label="Submarine trajectory")
ax1.legend()
fill_line = np.arange(0, 2000, 1)
plt.fill_between(fill_line,sonar)
ax1.figure.savefig("02_depth_aqua.png")

plt.rcParams["figure.figsize"] = (16 , 30)

ax2 = plt.subplot(111)
ax2.set_title("Depth")
ax2.plot(range(0, sonar.shape[0]), sonar[:], label="Depth") # range arbitrarily numbers x from 0 to the size of the 1D sonar array
ax2.set_xlabel("Across")
ax2.set_ylabel("Depth")
ax2.set_xlim([0, 2000])
ax2.set_ylim([1000000, 0])
ax2.plot(poscalc[0], poscalc[1], marker="x", markeredgecolor="red", markerfacecolor="red", label="Calculated position")
ax2.plot(traj[:,0], traj[:,1], label="Submarine trajectory")
ax2.legend()
fill_line = np.arange(0, 2000, 1)
plt.fill_between(fill_line,sonar)
ax2.figure.savefig("02_depth_geo.png")
