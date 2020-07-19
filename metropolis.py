import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
from scipy.stats import norm


N = 2000       # number of samples
scale = 0.002  # dummy scale
randwidth = 3  # discrete uniform [-randwidth,randwidth]
maxdx = 0.1    # trial range maxdx * [-randwidth,randwidth]


fig, ax = plt.subplots()
xdata, ydata = [0], [0]
ln, = plt.plot([], [], 'co', alpha=0.25)
lm, =  plt.plot([], [], 'ro', alpha=1.0)
title = ax.text(0.7, 0.9, "", bbox={
    'facecolor': 'w', 'alpha': 0.5, 'pad': 5}, transform=ax.transAxes)


def init():
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(0, 0.5)

    x = np.linspace(-3.5, 3.5, 1000)
    y = norm.pdf(x, 0, 1)
    plt.plot(x, y, 'k')
    return ln, lm, title


def update(frame):

    xtemp = xdata[-1] + maxdx*(np.random.randint(2*randwidth + 1) - randwidth)
    ytemp = norm.pdf(xtemp, 0, 1)
    rate = np.exp(0.5*(xdata[-1]**2-xtemp**2))
    state = "Reject"
    if np.random.rand() <= rate:
        state = "Accept"
        x = xtemp
    else:
        state = "Reject"
        x = xdata[-1]
    x = round(x, 2)
    xdata.append(x)
    ydata.append(scale * xdata.count(x))

    ln.set_data(xdata, ydata)
    lm.set_data(xtemp, ytemp)
    title.set_text('N = {}  {}'.format(frame + 1, state))

    return ln, lm, title


ani = FuncAnimation(fig, update, frames=N, init_func=init,
                    blit=True, interval=1, repeat=False)

ani.save("test.gif", writer='imagemagick', fps=60, dpi=60)
# plt.show()
