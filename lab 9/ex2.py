import numpy as np
import matplotlib.pyplot as plt

a_val = 0.9
b_val = 0.5
c_val = 1.0

steps = 50
t_arr = np.arange(steps)
ctrl = np.sin(0.2 * t_arr)

w_err = np.random.normal(0, 0.1, steps)
v_err = np.random.normal(0, 0.2, steps)

real_x = np.zeros(steps)
meas_y = np.zeros(steps)

real_x[0] = 2.0
meas_y[0] = c_val * real_x[0] + v_err[0]

for i in range(1, steps):
    real_x[i] = a_val * real_x[i-1] + b_val * ctrl[i] + w_err[i]
    meas_y[i] = c_val * real_x[i] + v_err[i]

est_x = np.zeros(steps)
est_x[0] = 0.0 

for i in range(1, steps):
    est_x[i] = a_val * est_x[i-1] + b_val * ctrl[i]

innov_err = np.zeros(steps)

for i in range(steps):
    innov_err[i] = meas_y[i] - c_val * est_x[i]

plt.figure(figsize=(10, 7))

plt.subplot(2, 1, 1)
plt.plot(t_arr, real_x, label='Actual State', color='teal', linewidth=2)
plt.plot(t_arr, est_x, label='Predicted State', color='coral', linestyle='--', linewidth=2)
plt.title('Prediction Simulation')
plt.xlabel('Time (t)')
plt.ylabel('State')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.subplot(2, 1, 2)
plt.plot(t_arr, innov_err, label='Innovation Error', color='olivedrab', linewidth=2)
plt.axhline(0, color='gray', linestyle='-', linewidth=1.5)
plt.title('Innovation over Time')
plt.xlabel('Time (t)')
plt.ylabel('Innovation')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.savefig('ex2.png', dpi=300, bbox_inches='tight')
plt.show()