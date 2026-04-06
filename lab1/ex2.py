#geerate noise obs : y(t) = x(t) + noise 
#use gaussian noise with mean 0 and standard deviation 2
#plot true state and observations on the same gra

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(51)
x = t
noise = np.random.normal(0, 2, size=len(t))
y = x + noise

plt.figure(figsize=(10, 6))
plt.plot(t, x, label='True State', color='blue', linewidth=2)
plt.scatter(t, y, label='Observations', color='red', s=15)
plt.xlabel('Time (t)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()