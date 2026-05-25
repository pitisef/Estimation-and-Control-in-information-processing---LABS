import numpy as np
import matplotlib.pyplot as plt

sys_a = 0.9
sys_c = 1.0
var_q = 0.01
var_r = 0.04
steps = 50
t_arr = np.arange(steps)

cov_pred = np.zeros(steps)
cov_upd = np.zeros(steps)

curr_p = 1.0
cov_upd[0] = curr_p

for i in range(1, steps):
    p_prior = sys_a * curr_p * sys_a + var_q
    cov_pred[i] = p_prior
    
    k_gain = (p_prior * sys_c) / (sys_c * p_prior * sys_c + var_r)
    curr_p = (1 - k_gain * sys_c) * p_prior
    cov_upd[i] = curr_p

plt.figure(figsize=(11, 6))

plt.plot(t_arr[1:], cov_pred[1:], label='Predicted Covariance', color='firebrick', linestyle='--', linewidth=2.5)
plt.plot(t_arr[1:], cov_upd[1:], label='Updated Covariance', color='dodgerblue', linewidth=2.5)

plt.title('Covariance Convergence Analysis')
plt.xlabel('Time Step')
plt.ylabel('Error Covariance (P)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.savefig('ex8.png', dpi=300, bbox_inches='tight')
plt.show()