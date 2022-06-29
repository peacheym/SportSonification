from tkinter import X
import matplotlib.pyplot as plt


f = open("./DATALOG.txt")

x_axis = []
y_axis = []
z_axis = []

for i in f:
    line = i.split(",")
    x_axis.append(line[0])
    y_axis.append(line[1])
    z_axis.append(line[2])
plt.plot(y_axis)
plt.show()