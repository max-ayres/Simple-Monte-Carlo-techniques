

import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0 ,1 ,10000)
y = np.random.uniform(0 ,1 ,10000)

ax = plt.axes()

line = np.linspace(0 ,1 ,10000)
liney = line

ax.plot(line, liney)

ben = np.array([])

for i in range(10000):
    if x[i] <= y[i]:
        ax.plot(x[i],y[i],'r.')
        plt.pause(0.01)
    else:
        ax.plot(x[i],y[i],'g.')
        ben = np.append(ben, x[i])
        plt.pause(0.01)
    
ax.hist(ben)