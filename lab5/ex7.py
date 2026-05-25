import numpy as np
import matplotlib.pyplot as plt

target_val = 10
samples = 1000

np.random.seed(42)
noise_data = np.random.normal(0, 1, samples)
measured_y = target_val + noise_data

calc_x = np.mean(measured_y)
diff_x = calc_x - target_val

print(f"Target:   {target_val:.4f}")
print(f"Estimate: {calc_x:.4f}")
print(f"Error:    {diff_x:.4f}")

plt.figure(figsize=(9, 5))
plt.hist(measured_y, bins=35, color='plum', edgecolor='black', alpha=0.75, label='Measurements')

plt.axvline(target_val, color='darkred', linestyle='-', linewidth=2.5, label=f'Target ({target_val})')
plt.axvline(calc_x, color='royalblue', linestyle='--', linewidth=2.5, label=f'Estimate ({calc_x:.4f})')

plt.title('Measurements Distribution vs Estimate')
plt.xlabel('Values')
plt.ylabel('Count')
plt.legend()

plt.savefig('ex7.png', dpi=300, bbox_inches='tight')
plt.show()