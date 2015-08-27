import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#with open('Selected.txt') as file:
	#lines = file.readlines()
#print len(lines)s

GPSData = np.loadtxt('Selected.txt', skiprows = 1)
print GPSData
print ('The dimensions of the array', GPSData.shape)

xGPS = GPSData[:,0]
yGPS = GPSData[:,1]
zGPS = GPSData[:,2]

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')


#print xGPS
#print yGPS
#print zGPS


#ax.plot(xGPS, yGPS, zGPS, label='The UAV Landing Curve')
ax.scatter(xGPS, yGPS, zGPS, c='r', marker='o', linewidths=0, alpha=0.7)

ax.legend()
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

#plt.style.use(['dark_background', 'presentation'])
plt.show()