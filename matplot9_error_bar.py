import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2 * np.pi)
y_sin = np.sin(x)
y_cos = np.cos(x)
#plt.errorbar(x, y_sin, 0.2)
#plt.errorbar(x, y_cos, 0.2)
#plt.show()

def errorfill(x, y, yerr, color=None, alpha_fill=0.3, ax=None):
    ax = ax if ax is not None else plt.gca()
    if color is None:
        color = ax._get_lines.color_cycle.next()
    if np.isscalar(yerr) or len(yerr) == len(y):
        ymin = y - yerr
        ymax = y + yerr
    elif len(yerr) == 2:
        ymin, ymax = yerr
    ax.plot(x, y, color=color)
    ax.fill_between(x, ymax, ymin, color=color, alpha=alpha_fill)

errorfill(x, y_sin, 0.2)
errorfill(x, y_cos, 0.2)
plt.show()