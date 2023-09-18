
import numpy as np
import matplotlib.pyplot as plt

N = 70
x = 0
y = 0
rms = 0
t = np.arange(0, 10, 0.1)
z = 0

walk = np.random.uniform(0,1000,N)

fig = plt.figure()
ax1 = fig.add_axes([0.07, 0.2, 0.4, 0.65])
ax2 = fig.add_axes([0.55, 0.2, 0.4, 0.65])

ax1.set_xlim(-15, 15)
ax1.set_ylim(-15, 15)
ax2.set_xlim(0,7)
ax2.set_ylim(0,12)

ax1.set_xlabel('$x$', size = 20)
ax1.set_ylabel('$y$', size = 20)
ax2.set_xlabel('$t$', size = 20)
ax2.set_ylabel('$rms$', size = 20)

ax1.plot(x, y, color = 'black')

colors = ['r', 'b', 'g', 'orange']

for z in range(4):
    for i in range(N):
        if walk[i] >= 750:
            ax1.plot([x, x + 1], [y, y], color = colors[z])
            x = x + 1
            ax2.plot([t[i], t[i + 1]], [rms, np.sqrt(x**2 + y**2)], color = colors[z])
            rms = np.sqrt(x**2 + y**2)
            plt.pause(0.1)
        elif walk[i] >= 500:
            ax1.plot([x, x - 1], [y, y], color = colors[z])
            x = x - 1
            ax2.plot([t[i], t[i + 1]], [rms, np.sqrt(x**2 + y**2)], color = colors[z])
            rms = np.sqrt(x**2 + y**2)
            plt.pause(0.1)
        elif walk[i] >= 250:
            ax1.plot([x, x], [y, y + 1], color = colors[z])
            y = y + 1
            ax2.plot([t[i], t[i + 1]], [rms, np.sqrt(x**2 + y**2)], color = colors[z])
            rms = np.sqrt(x**2 + y**2)
            plt.pause(0.1)
        else:
            ax1.plot([x, x], [y, y - 1], color = colors[z])
            y = y - 1
            ax2.plot([t[i], t[i + 1]], [rms, np.sqrt(x**2 + y**2)], color = colors[z])
            rms = np.sqrt(x**2 + y**2)
            plt.pause(0.1)
    x = 0
    y = 0
    rms = 0
    t = np.arange(0, 10, 0.1)
    walk = np.random.uniform(0,1000,N)
    z = z + 1
