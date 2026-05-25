import numpy as np
import matplotlib.pyplot as plt

norm_vals = np.random.normal(0, 1, 10000)
uni_vals = np.random.uniform(-np.sqrt(3), np.sqrt(3), 10000)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(norm_vals, bins=45, density=True, color='dodgerblue', edgecolor='black')
plt.title('Normal Distribution')
plt.xlabel('Data')
plt.ylabel('Probability')

plt.subplot(1, 2, 2)
plt.hist(uni_vals, bins=45, density=True, color='mediumseagreen', edgecolor='black')
plt.title('Uniform Distribution')
plt.xlabel('Data')
plt.ylabel('Probability')

plt.tight_layout()
plt.savefig('ex4.png')
plt.show()