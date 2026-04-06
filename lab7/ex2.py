import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
y = np.array([40, 42, 45])

A = np.array([[1, 1], 
              [2, 1], 
              [3, 1]])
Y = y.reshape(-1, 1)

theta = np.linalg.lstsq(A, Y, rcond=None)[0]
a = theta[0][0]
b = theta[1][0]

print(f"Results: a = {a:.2f}, b = {b:.2f}")

plt.scatter(x, y, color='red', label='puncte')
plt.plot(x, a*x + b, label=f'linia: y={a:.1f}x+{b:.2f}')
plt.xlabel('Time')
plt.ylabel('Humidity')
plt.legend()
plt.grid(True)
plt.show()