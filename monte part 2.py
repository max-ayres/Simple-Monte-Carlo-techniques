

import numpy as np
import matplotlib.pyplot as plt

N=1000

xr = np.random.uniform(-np.pi/2 ,np.pi/2 ,N)
yr = np.random.uniform(0, 1, N)

y = np.exp(-np.abs(xr)) * np.cos(xr)

ax = plt.axes()
ax.plot(xr,y,'.')

Nu = 0

for i in range(N):
    if y[i] > yr[i]:
        ax.plot(xr[i], yr[i], 'g.')
        Nu = Nu + 1
        plt.pause(0.01)
    else:
        ax.plot(xr[i], yr[i], 'r.')
        plt.pause(0.01)
        
val = (np.pi/2 + np.pi/2) * 1 * (Nu/N)
print('The value of the integral is', val)