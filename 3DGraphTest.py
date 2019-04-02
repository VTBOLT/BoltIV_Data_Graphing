import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = []  
y = []
z = []
x.append(float(input('input the x coordinate: ')))
y.append(float(input('input the y coordinate: ')))
z.append(float(input('input the z coordinate: ')))

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.scatter(x,y,z)

ax.plot([-2,2],[0,0],[0,0])
ax.plot([0,0],[-2,2],[0,0])
ax.plot([0,0],[0,0],[-2,2])

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-2,2)
ax.xaxis._axinfo['jugled'] = (0,0,0)
ax.spines['right'].set_position('zero')
fig.show()

while 1:
    x.append(float(input('input the x coordinate: ')))
    y.append(float(input('input the y coordinate: ')))
    z.append(float(input('input the z coordinate: ')))
    ax.scatter(x,y,z)
    fig.show()