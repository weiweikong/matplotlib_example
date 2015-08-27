import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import cm

import pylab
from pylab import rcParams
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

def my_annotate(ax, s, xy_arr=[], *args, **kwargs):
  ans = []
  an = ax.annotate(s, xy_arr[0], *args, **kwargs)
  ans.append(an)
  d = {}
  try:
    d['xycoords'] = kwargs['xycoords']
  except KeyError:
    pass
  try:
    d['arrowprops'] = kwargs['arrowprops']
  except KeyError:
    pass
  for xy in xy_arr[1:]:
    an = ax.annotate(s, xy, alpha=0.0, xytext=(0,0), textcoords=an, **d)
    ans.append(an)
  return ans

ax = plt.gca()
ax.plot([1,2,3,4],[1,4,2,6])
my_annotate(ax,
            'Test',
            xy_arr=[(2,4), (3,2), (4,6)], xycoords='data',
            xytext=(30, -80), textcoords='offset points',
            bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
            arrowprops=dict(arrowstyle="-|>",
                            connectionstyle="arc3,rad=0.2",
                            fc="w"))
plt.show()