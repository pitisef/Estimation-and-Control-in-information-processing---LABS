#implement a moving average estimator
#compute an estimated signal from noisy obs
#plot true state, noisy obs and estimated state

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(51)
x = t
y = x + np.random.normal(0, 2, 51)

window_size = 5
y_hat = np.convolve(y, np.ones(window_size)/window_size, mode='same')

plt.figure(figsize=(10, 6))
plt.plot(t, x, 'k--', label='True State', linewidth=1.5)
plt.scatter(t, y, color='red', s=20, alpha=0.6, label='Noisy Observations')
plt.plot(t, y_hat, 'g-', label='Estimated (Moving Average)', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()