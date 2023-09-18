
import numpy as np
import matplotlib.pyplot as plt

b = 10
a = 5
N = 1000

x = np.random.uniform(-b, b, N)
y = np.random.uniform(-b, b, N)
z = np.random.uniform(-b, b, N)

cube = 20**3

def pierre(x, y, z):
    pierre = (np.sqrt(x**2 + y**2) - (b + a)/2)**2 + z**2
    return pierre 
    
Nu = 0

for i in range(1000):
    if 6.25 >= pierre(x[i], y[i], z[i]):
        Nu = Nu + 1
    
val = (Nu/N) * 20 * 20 * 20

print('The value of the integral is', val)