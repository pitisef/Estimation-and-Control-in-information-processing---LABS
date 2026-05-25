import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

delta_t = 1
sys_a = np.array([[1, delta_t], [0, 1]])
sys_c = np.array([[1, 0]])
sys_q = np.array([[0.01, 0], [0, 0.01]])
sys_r = np.array([[1.0]])
sys_i = np.eye(2)

steps = 50
t_arr = np.arange(steps)

real_x = np.zeros((2, steps))
meas_y = np.zeros(steps)

real_x[:, 0] = [0, 2]

for i in range(1, steps):
    w_noise = np.random.multivariate_normal([0, 0], sys_q)
    real_x[:, i] = sys_a @ real_x[:, i-1] + w_noise
    
v_noise = np.random.normal(0, np.sqrt(sys_r[0,0]), steps)

for i in range(steps):
    meas_y[i] = sys_c @ real_x[:, i] + v_noise[i]

est_x = np.zeros((2, steps))
est_x[:, 0] = [0, 0]
cov_p = np.array([[10, 0], [0, 10]])

for i in range(1, steps):
    x_pri = sys_a @ est_x[:, i-1]
    p_pri = sys_a @ cov_p @ sys_a.T + sys_q
    
    k_gain = p_pri @ sys_c.T @ np.linalg.inv(sys_c @ p_pri @ sys_c.T + sys_r)
    
    innov = np.array([meas_y[i]]) - sys_c @ x_pri
    est_x[:, i] = x_pri + k_gain @ innov
    cov_p = (sys_i - k_gain @ sys_c) @ p_pri

plt.figure(figsize=(11, 9))

plt.subplot(2, 1, 1)
plt.plot(t_arr, real_x[0, :], label='Actual Position', color='navy', linewidth=2.5)
plt.plot(t_arr, est_x[0, :], label='Estimated Position', color='crimson', linestyle='--', linewidth=2.5)
plt.scatter(t_arr, meas_y, label='Noisy Y', color='darkgray', s=20, alpha=0.6)
plt.title('Position Estimation Analysis')
plt.xlabel('Time Step')
plt.ylabel('Position')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(t_arr, real_x[1, :], label='Actual Velocity', color='forestgreen', linewidth=2.5)
plt.plot(t_arr, est_x[1, :], label='Estimated Velocity', color='darkorange', linestyle='--', linewidth=2.5)
plt.title('Velocity Estimation Analysis')
plt.xlabel('Time Step')
plt.ylabel('Velocity')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.savefig('ex9.png', dpi=300, bbox_inches='tight')
plt.show()