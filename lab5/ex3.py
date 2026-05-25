import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
u_data = np.random.uniform(0, 1, 1000)

calc_mean = np.mean(u_data)
true_mean = 0.5

print(f"Calculated Mean: {calc_mean:.4f}")
print(f"Expected Mean: {true_mean:.4f}")
print(f"Error: {abs(calc_mean - true_mean):.4f}")

plt.hist(u_data, bins=25, color='gold', edgecolor='black')

plt.axvline(calc_mean, color='purple', linestyle='--', linewidth=2, label=f'Calculated ({calc_mean:.4f})')
plt.axvline(true_mean, color='navy', linestyle='-', linewidth=2, label=f'Expected ({true_mean})')

plt.title('Uniform Distribution: Expected vs Calculated Mean')
plt.xlabel('Data Values')
plt.ylabel('Counts')
plt.legend()

plt.savefig('ex3.png', dpi=300, bbox_inches='tight')
plt.show()