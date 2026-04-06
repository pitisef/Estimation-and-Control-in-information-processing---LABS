#task 5: smart home energy model
#data: energy vs time
#fit linear model
#interpret slope as consumption rate
#plot data and fitted line
#invented values

import numpy as np
import matplotlib.pyplot as plt

time = np.array([1, 2, 3, 4, 5])
energy = np.array([1.5, 2.8, 4.2, 5.5, 7.0])

A = np.vstack([time, np.ones(len(time))]).T
Y = energy.reshape(-1, 1)

theta = np.linalg.inv(A.T @ A) @ A.T @ Y
a, b = theta[0][0], theta[1][0]

print(f"Consumption Rate: {a:.2f} kWh/h")

plt.scatter(time, energy, color='black', label='energy')
plt.plot(time, a*time + b, color='green', label=f'Fit: {a:.2f}x + {b:.2f}')
plt.xlabel('time (hrs)')
plt.ylabel('energy (kWh)')
plt.title('Smart Home Energy Consumption')
plt.legend()
plt.grid(True)
plt.show()