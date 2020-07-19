import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


N = 2000  # number of samples


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'co', alpha=0.25)
title = ax.text(0.6, 0.9, "", bbox={
    'facecolor': 'w', 'alpha': 0.5, 'pad': 5}, transform=ax.transAxes)


def init():
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    x = np.linspace(0, 1, 1000)
    y = np.sqrt(1-x**2)
    plt.plot(x, y, 'k')
    return ln, title


def update(frame):
    x = np.random.rand()
    y = np.sqrt(1 - x ** 2)

    xdata.append(x)
    ydata.append(y)

    ln.set_data(xdata, ydata)
    title.set_text('N = {} $\pi \sim$ {:.5f}'.format(
        frame + 1, 4.0*sum(ydata)/(frame + 1)))

    return ln, title


ani = FuncAnimation(fig, update, frames=N, init_func=init,
                    blit=True, interval=1, repeat=False)
plt.show()
