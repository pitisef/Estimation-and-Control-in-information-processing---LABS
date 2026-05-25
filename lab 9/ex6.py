import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

sys_a = 0.9
sys_b = 0.5
sys_c = 1.0
steps = 50
t_arr = np.arange(steps)

ctrl_in = np.sin(0.2 * t_arr)
w_noise = np.random.normal(0, 0.1, steps)
v_noise = np.random.normal(0, 0.2, steps)

actual_x = np.zeros(steps)
meas_y = np.zeros(steps)

actual_x[0] = 2.0
meas_y[0] = sys_c * actual_x[0] + v_noise[0]

for i in range(1, steps):
    actual_x[i] = sys_a * actual_x[i-1] + sys_b * ctrl_in[i] + w_noise[i]
    meas_y[i] = sys_c * actual_x[i] + v_noise[i]

def kalman_filter(var_q, var_r):
    est_x = np.zeros(steps)
    cov_p = 1.0
    for i in range(1, steps):
        pri_x = sys_a * est_x[i-1] + sys_b * ctrl_in[i]
        pri_p = sys_a * cov_p * sys_a + var_q
        
        k_gain = (pri_p * sys_c) / (sys_c * pri_p * sys_c + var_r)
        
        est_x[i] = pri_x + k_gain * (meas_y[i] - sys_c * pri_x)
        cov_p = (1 - k_gain * sys_c) * pri_p
    return est_x

test_q_vals = [0.0001, 0.01, 1]
fixed_r = 0.04

plt.figure(figsize=(11, 10))

plt.subplot(2, 1, 1)
plt.plot(t_arr, actual_x, label='Actual Data', color='darkslategray', linewidth=2.5)
plt.scatter(t_arr, meas_y, label='Recorded Y', color='silver', s=15)
for q_test in test_q_vals:
    calc_x = kalman_filter(q_test, fixed_r)
    plt.plot(t_arr, calc_x, label=f'Q={q_test}')
plt.title('Effect of Q Variance on Estimation')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

fixed_q = 0.01
test_r_vals = [0.01, 0.5, 5]

plt.subplot(2, 1, 2)
plt.plot(t_arr, actual_x, label='Actual Data', color='darkslategray', linewidth=2.5)
plt.scatter(t_arr, meas_y, label='Recorded Y', color='silver', s=15)
for r_test in test_r_vals:
    calc_x = kalman_filter(fixed_q, r_test)
    plt.plot(t_arr, calc_x, label=f'R={r_test}')
plt.title('Effect of R Variance on Estimation')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('ex6.png', dpi=300, bbox_inches='tight')
plt.show()