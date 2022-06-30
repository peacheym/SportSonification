from cProfile import label
from tkinter import X
import matplotlib.pyplot as plt


f = open("./DATALOG.txt")

x_axis = []
y_axis = []
z_axis = []

for i in f:
    line = i.split(",")
    x_axis.append(float(line[0]))
    y_axis.append(float(line[1]))
    z_axis.append(1-float(line[2])) # Z Axis seems to hover around 1 rather than 0 like X & Y.

# Plot all 3 axes on one
plt.plot([i for i in range(len(x_axis))], x_axis, label="X Axis")
plt.plot([i for i in range(len(y_axis))], y_axis, label="Y Axis")
plt.plot([i for i in range(len(z_axis))], z_axis, label="Z Axis")

plt.legend()
plt.show()