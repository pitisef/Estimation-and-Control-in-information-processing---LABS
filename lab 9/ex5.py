import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

sys_a = 0.9  
sys_b = 0.5  
sys_c = 1.0  
var_q = 0.01 
var_r = 0.04 

steps = 50
t_arr = np.arange(steps)

ctrl_u = np.sin(0.2 * t_arr) 
w_noise = np.random.normal(0, np.sqrt(var_q), steps)
v_noise = np.random.normal(0, np.sqrt(var_r), steps)

actual_x = np.zeros(steps)
meas_y = np.zeros(steps)

actual_x[0] = 2.0 
meas_y[0] = sys_c * actual_x[0] + v_noise[0]

for i in range(1, steps):
    actual_x[i] = sys_a * actual_x[i-1] + sys_b * ctrl_u[i] + w_noise[i]
    meas_y[i] = sys_c * actual_x[i] + v_noise[i]

pred_x = np.zeros(steps)
pred_x[0] = 0.0 

for i in range(1, steps):
    pred_x[i] = sys_a * pred_x[i-1] + sys_b * ctrl_u[i]

kf_x = np.zeros(steps)
kf_x[0] = 0.0 
cov_p = 1.0        

for i in range(1, steps):
    prior_x = sys_a * kf_x[i-1] + sys_b * ctrl_u[i]
    prior_p = sys_a * cov_p * sys_a + var_q
    
    k_gain = (prior_p * sys_c) / (sys_c * prior_p * sys_c + var_r) 
    
    kf_x[i] = prior_x + k_gain * (meas_y[i] - sys_c * prior_x)
    cov_p = (1 - k_gain * sys_c) * prior_p

err_pred = np.mean((actual_x - pred_x)**2)
err_kf = np.mean((actual_x - kf_x)**2)

print(f"MSE (Prediction): {err_pred:.4f}")
print(f"MSE (Kalman):     {err_kf:.4f}")

plt.figure(figsize=(11, 7))

plt.plot(t_arr, actual_x, label='Actual $x(t)$', color='mediumblue', linewidth=2)
plt.plot(t_arr, pred_x, label='Predicted Only', color='crimson', linestyle='--', linewidth=2)
plt.plot(t_arr, kf_x, label='Kalman Filter', color='forestgreen', linestyle='-.', linewidth=2)
plt.scatter(t_arr, meas_y, label='Measured $y(t)$', color='darkgray', s=20, alpha=0.6)

plt.title('Prediction vs Kalman Filter Estimation')
plt.xlabel('Time Step ($t$)')
plt.ylabel('State')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.savefig('ex5.png', dpi=300, bbox_inches='tight')
plt.show()