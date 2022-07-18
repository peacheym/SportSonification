from hashlib import new
import matplotlib.pyplot as plt
import numpy as np


def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth - 5


f = open("./mixeddata.txt")

x_axis = []
y_axis = []
z_axis = []
avg = []
vel = []

last_vel = 0

for i in f:
    line = i.split(",")
    x_axis.append(float(line[0]))
    y_axis.append(float(line[1]))
    # Z Axis seems to hover around 1 rather than 0 like X & Y.
    z_axis.append(1-float(line[2]))

    # Average of three axis
    avg_a = (float(line[0]) + float(line[1]) + float(line[0]))/3 - 5
    avg.append(avg_a)

# Plot all 3 axes on one
plt.plot([i for i in range(len(x_axis))], x_axis, label="X Axis")
plt.plot([i for i in range(len(y_axis))], y_axis, label="Y Axis")
plt.plot([i for i in range(len(z_axis))], z_axis, label="Z Axis")


window = 10
avg_smooth = smooth(avg, window)

avg_smooth[:window] = -10
avg_smooth[-window:] = -10

print(avg_smooth)

plt.plot([i for i in range(len(avg))], avg, label="Average")
plt.plot([i for i in range(len(avg))], avg_smooth, label="Smooth", linewidth=3)


plt.legend()
plt.show()