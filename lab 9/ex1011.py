import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

total_steps = 50
t_array = np.arange(total_steps)
sys_a = 0.9
sys_b = 0.5
sys_c = 1.0
var_q = 0.01
var_r = 0.04
ctrl_gain = 0.5

actual_x = np.zeros(total_steps)
calc_x = np.zeros(total_steps)
ctrl_in = np.zeros(total_steps)

actual_x[0] = 2.0
pri_x = 0.0
cov_p = 1.0

for i in range(total_steps):
    v_noise = np.random.normal(0, np.sqrt(var_r))
    meas_y = sys_c * actual_x[i] + v_noise
    
    k_gain = (cov_p * sys_c) / (sys_c * cov_p * sys_c + var_r)
    calc_x[i] = pri_x + k_gain * (meas_y - sys_c * pri_x)
    cov_p = (1 - k_gain * sys_c) * cov_p
    
    ctrl_in[i] = -ctrl_gain * calc_x[i]
    
    if i < total_steps - 1:
        w_noise = np.random.normal(0, np.sqrt(var_q))
        actual_x[i+1] = sys_a * actual_x[i] + sys_b * ctrl_in[i] + w_noise
        pri_x = sys_a * calc_x[i] + sys_b * ctrl_in[i]
        cov_p = sys_a * cov_p * sys_a + var_q

t_nl = np.arange(30)
state_nl = np.zeros(30)
state_nl[0] = 0.5
input_nl = 0.2 * np.sin(t_nl)

for i in range(29):
    state_nl[i+1] = state_nl[i] + 0.1 * (state_nl[i]**2) + input_nl[i]

plt.figure(figsize=(11, 10))

plt.subplot(3, 1, 1)
plt.plot(t_array, actual_x, label='Actual State', color='navy', linewidth=2.5)
plt.plot(t_array, calc_x, label='Calculated State', color='crimson', linestyle='--', linewidth=2.5)
plt.title('Closed Loop Feedback System')
plt.ylabel('State Value')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.subplot(3, 1, 2)
plt.step(t_array, ctrl_in, label='Control Signal', color='darkmagenta', linewidth=2.5)
plt.ylabel('Input Value')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.subplot(3, 1, 3)
plt.plot(t_nl, state_nl, label='Nonlinear State', color='forestgreen', linewidth=2.5)
plt.title('Nonlinear Simulation')
plt.xlabel('Time Step')
plt.ylabel('State Value')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.savefig('ex10_11.png', dpi=300, bbox_inches='tight')
plt.show()