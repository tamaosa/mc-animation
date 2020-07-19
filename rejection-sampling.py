import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter


N = 400       # number of samples
scale = 0.02  # dummy scale
d = 10        # discrete uniform [0,d]/d


fig, ax = plt.subplots()
xdata, ydata = [], []
xtemp, ytemp = 0, 0
ln, = plt.plot([], [], 'co', alpha=0.25)
lm, =  plt.plot([], [], 'ro', alpha=1.0)
title = ax.text(0.7, 0.9, "", bbox={
    'facecolor': 'w', 'alpha': 0.5, 'pad': 5}, transform=ax.transAxes)


def init():
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    x = np.linspace(0, 1, 1000)
    y = np.sqrt(1-x**2)
    plt.plot(x, y, 'k')
    return ln, lm, title


def update(frame):

    x = np.random.randint(d+1)/d
    y = np.random.rand()

    xtemp = x
    ytemp = y
    state = "Reject"
    if x * x + y * y <= 1:
        xdata.append(x)
        ydata.append(scale*xdata.count(x))
        state = "Accept"

    ln.set_data(xdata, ydata)
    lm.set_data(xtemp, ytemp)
    title.set_text('N = {}  {}'.format(frame + 1, state))

    return ln, lm, title


ani = FuncAnimation(fig, update, frames=N, init_func=init,
                    blit=True, interval=60, repeat=False)
plt.show()
