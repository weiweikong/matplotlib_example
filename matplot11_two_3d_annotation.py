import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

points = np.array([(1,1,1), (2,2,2)])
labels = ['billy', 'bobby']

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
xs, ys, zs = np.split(points, 3, axis=1)
sc = ax.scatter(xs,ys,zs)

# if this code is placed inside a function, then
# we must use a predefined global variable so that
# the update function has access to it. I'm not
# sure why update_positions() doesn't get access
# to its enclosing scope in this case.
global labels_and_points
labels_and_points = []

for txt, x, y, z in zip(labels, xs, ys, zs):
    x2, y2, _ = proj3d.proj_transform(x,y,z, ax.get_proj())
    label = plt.annotate(
        txt, xy = (x2, y2), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    labels_and_points.append((label, x, y, z))


def update_position(e):
    for label, x, y, z in labels_and_points:
        x2, y2, _ = proj3d.proj_transform(x, y, z, ax.get_proj())
        label.xy = x2,y2
        label.update_positions(fig.canvas.renderer)
    fig.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', update_position)

plt.show()