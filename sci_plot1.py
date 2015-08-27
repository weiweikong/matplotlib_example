import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import cm

import pylab
from pylab import rcParams
from mpl_toolkits.mplot3d import Axes3D

import mpl_toolkits.mplot3d as a3

from mpl_toolkits.mplot3d import proj3d

import numpy as np
import matplotlib.colors as colors
import scipy as sp
# with open('Selected.txt') as file:
#lines = file.readlines()
# print len(lines)

# test

#pylab.rcParams['figure.figsize'] = (8.0, 4.0)

GPSData = np.loadtxt('Selectet_orginal_GPS.txt', skiprows=1)
imgData = np.loadtxt('Selectet_orginal_Image.txt', skiprows=1)

# print GPSData
print('The dimensions of the GPS array', GPSData.shape)
print('The dimensions of the Image array', imgData.shape)


xGPS = GPSData[:, 0]
yGPS = GPSData[:, 1]
zGPS = GPSData[:, 2]

xImg = imgData[:, 0]
yImg = imgData[:, 1]
zImg = imgData[:, 2]


mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.axis('equal')

# print xGPS
# print yGPS
# print zGPS

# -------- Draw Landing Trajectory ------- #
gpsLegend = ax.plot(xGPS, yGPS, zGPS, color=[
                    31/255., 119/255., 180/255.], marker='o', mec='none', markersize=3.0, alpha=0.3, label='The GPS Data of UAV')
# ax.axis('equal')
imgLegend = ax.plot(xImg, yImg, zImg, color=[
                    214/255., 19/255., 40/255.], marker='o', mec='none', markersize=4.0, alpha=0.5, label='The Image Data of UAV')
# ax.axis('equal')
projectLegend = ax.plot(xGPS, yGPS, 0, 'g--', mec='none',
                        linewidth=2.0, alpha=0.8, label='The UAV Landing Curve')

# ax.legend([, ], ['abc', 'def'], numpoints = 1)

ax.legend()
ax.set_xlabel('X Coordinate (m)')
ax.set_ylabel('Y Coordinate (m)')
ax.set_zlabel('Z Coordinate (m)')


# ----- Draw Projection Trajectory ---- #
firstLineX = np.array([xImg[0], xImg[0], xImg[0]])
firstLineY = np.array([yImg[0], yImg[0], yImg[0]])
firstLineZ = np.array([zImg[0], zImg[0], 0])
ax.plot(firstLineX, firstLineY, firstLineZ, 'g--')


#el = ax.plot([1],[2],[3], 'go')
firstPoint2DX, firstPoint2DY, _ = proj3d.proj_transform(
    xImg[0], yImg[0], zImg[0], ax.get_proj())
print('First 2D Point', firstPoint2DX, firstPoint2DY)

label = pylab.annotate(
    "Catching Point",
    xy=(firstPoint2DX, firstPoint2DY),
    xytext=(-20, 20),
    textcoords='offset points',
    ha='right',
    va='bottom',
    arrowprops=dict(arrowstyle='fancy', color="0.5", shrinkB=5, connectionstyle='arc3,rad=0'))


#ax.scatter(xImg, yImg, zImg, c='r', s = 16, marker='o', linewidths=0, alpha=1.0)
#ax.scatter(xGPS, yGPS, zGPS, c='b', s = 7, marker='o', linewidths=0, alpha=0.7)


# ------------- Draw Airport ------------#
xCenter = 55
yCenter = -50
Length = 200
Width = 50

x1 = xCenter + Width
y1 = yCenter + Length
x2 = xCenter + Width
y2 = yCenter - Length
x3 = xCenter - Width
y3 = yCenter - Length
x4 = xCenter - Width
y4 = yCenter + Length

z = -2

tri = sp.rand(3, 3)
print tri

xVector = [x1, x2, x3, x4]
yVector = [y1, y2, y3, y4]
zVector = [z, z, z, z]
airportPos = [zip(xVector, yVector, zVector)]
#airportPos = np.array([ (x1,x2,x3,x4), (y1,y2,y3,y4),(z,z,z,z) ] )
print airportPos

airportHandle = a3.art3d.Poly3DCollection(airportPos)
airportHandle.set_color(colors.rgb2hex([23/255., 190/255., 207/255.]))
ax.add_collection3d(airportHandle)


# ------------- Update Annotation Postion -----------#

def update_position(e):
    firstPoint2DX, firstPoint2DY, _ = proj3d.proj_transform(
        xImg[0], yImg[0], zImg[0], ax.get_proj())
    label.xy = firstPoint2DX, firstPoint2DY
    label.update_positions(fig.canvas.renderer)
    fig.canvas.draw()

fig.canvas.mpl_connect('button_release_event', update_position)


ax.set_xlim(-600, 200)
ax.set_ylim(-400, 800)
ax.set_zlim(-10, 100)


plt.grid()
plt.show()
