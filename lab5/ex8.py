import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mu_vec = [0, 0]
covariance = [[1.0, 0.8], 
              [0.8, 1.0]]

v1, v2 = np.random.multivariate_normal(mu_vec, covariance, 1000).T

calc_cov = np.cov(v1, v2)

print("Calculated Covariance Matrix:")
print(calc_cov)
print(f"\nCalculated Covariance (V1, V2): {calc_cov[0, 1]:.4f}")

plt.figure(figsize=(9, 7))
plt.scatter(v1, v2, alpha=0.6, color='mediumorchid', edgecolor='black')

plt.title('Correlated Random Variables: Scatter Plot')
plt.xlabel('X Data')
plt.ylabel('Y Data')
plt.grid(True, linestyle=':', alpha=0.6)

plt.savefig('ex8.png', dpi=300, bbox_inches='tight')
plt.show()