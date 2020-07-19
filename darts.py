import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


N = 2000  # number of samples


fig, ax = plt.subplots()
x1data, y1data = [], []
x2data, y2data = [], []
ln, = plt.plot([], [], 'co', alpha=0.25)
lm, = plt.plot([], [], 'ro', alpha=0.25)
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
    return ln, lm, title


def update(frame):
    x = np.random.rand()
    y = np.random.rand()

    if x * x + y * y <= 1:
        x1data.append(x)
        y1data.append(y)
    else:
        x2data.append(x)
        y2data.append(y)

    ln.set_data(x1data, y1data)
    lm.set_data(x2data, y2data)
    title.set_text('N = {} $\pi \sim$ {:.5f}'.format(
        frame + 1, 4.0*len(x1data)/(frame + 1.0)))

    return ln, lm, title


ani = FuncAnimation(fig, update, frames=N, init_func=init,
                    blit=True, interval=1, repeat=False)
plt.show()
