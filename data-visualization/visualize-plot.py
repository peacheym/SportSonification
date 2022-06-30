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
    

fig, axs = plt.subplots(3, 1, sharex=True)
    

axs[0] = plt.plot(x_axis)
axs[1] = plt.plot(y_axis)    
axs[2] = plt.plot(z_axis)
plt.show()