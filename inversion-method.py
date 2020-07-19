import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter


N = 2000   # number of samples
XMAX = 10
YMAX = 1000


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'co', alpha=0.25)
title = ax.text(0.8, 0.9, "", bbox={
    'facecolor': 'w', 'alpha': 0.5, 'pad': 5}, transform=ax.transAxes)


def init():
    ax.set_xlabel('x')
    ax.set_ylabel('h(x)')
    ax.set_xlim(0, XMAX)
    ax.set_ylim(0, YMAX)
    ax.set_xticks(np.linspace(0, XMAX, 5))
    ax.set_yticks(np.linspace(0, YMAX, 5))
    return ln, title


def update(frame):
    u = np.random.rand()
    x = int(-2.0 * np.log(u))  # exponential distribution
    xdata.append(x)
    ydata.append(xdata.count(x))

    ln.set_data(xdata, ydata)
    title.set_text('N = {}'.format(frame + 1))

    return ln, title


ani = FuncAnimation(fig, update, frames=N, init_func=init,
                    blit=True, interval=1, repeat=False)
plt.show()
