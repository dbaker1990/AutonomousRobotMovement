import laspy
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from pandas import *
from matplotlib import cm


data = read_csv("Lidar_Information.csv")

x = data['X'].tolist()
x1 = []
y = data['Y'].tolist()
y1 = []
z = data['Z'].tolist()
z1 = []
time = data['Time'].tolist()


for index, (xi,yi,zi,timei) in enumerate(zip(x,y,z,time)):
    if index == 50000: break
    
    if zi <= 0.5 and timei == 0.0:
        x1.append(xi)
        y1.append(yi)
        z1.append(zi)
    
   

x_mask = np.array(x1)
y_mask = np.array(y1)
z_mask = np.array(z1)

fig = plt.figure(figsize=(100,100))
ax = plt.axes(projection="3d")


ax.scatter3D(x_mask,y_mask,z_mask,c=z_mask, cmap = cm.twilight)
plt.show()
