#consider a simple system: x(t+1) = x(t) + 1
#generate the true state x(t) for 50 time steps
#plot the evolution of the true state 


import numpy as np
import matplotlib.pyplot as plt

t = np.arange(51)
x = t

plt.figure(figsize=(8, 5))
plt.plot(t, x, 'b-', linewidth=2)
plt.title('System Evolution: x(t+1) = x(t) + 1')
plt.xlabel('Time (t)')
plt.ylabel('True State x(t)')
plt.grid(True)
plt.show()