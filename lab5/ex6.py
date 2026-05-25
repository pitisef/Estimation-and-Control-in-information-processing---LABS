import numpy as np
import matplotlib.pyplot as plt

actual_val = 10
num_samples = 1000

np.random.seed(42)
random_error = np.random.normal(0.0, 1.0, num_samples)
measured_vals = actual_val + random_error

plt.figure(figsize=(11, 5))
plt.plot(measured_vals, marker='.', linestyle='', markersize=5, alpha=0.6, color='darkcyan', label='Recorded Data')

plt.axhline(actual_val, color='black', linewidth=2.5, label=f'Actual (x={actual_val})')

plt.title('Noisy Measurement Simulation')
plt.xlabel('Sample Index')
plt.ylabel('Recorded Value')
plt.legend()

plt.savefig('ex6.png', dpi=300, bbox_inches='tight')
plt.show()