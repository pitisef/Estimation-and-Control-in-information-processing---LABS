import numpy as np
import matplotlib.pyplot as plt

time_steps = 30
sys_A, sys_B, sys_C = 1, 1, 1
ctrl_u = 1
init_val = 0

q_noise = 0.01  
r_noise = 0.5   

actual_x = np.zeros(time_steps)
obs_y = np.zeros(time_steps)
kalman_est = np.zeros(time_steps)
cov_hist = np.zeros(time_steps)
gain_hist = np.zeros(time_steps)

curr_x = init_val
curr_est = 0
curr_p = 1

for i in range(time_steps):
    actual_x[i] = curr_x
    v_noise = np.random.normal(0, np.sqrt(r_noise))
    obs_y[i] = sys_C * curr_x + v_noise
    
    w_noise = np.random.normal(0, np.sqrt(q_noise))
    curr_x = sys_A * curr_x + sys_B * ctrl_u + w_noise
    
    pred_x = sys_A * curr_est + sys_B * ctrl_u
    pred_p = sys_A * curr_p * sys_A + q_noise

    k_gain = pred_p * sys_C * (1.0 / (sys_C * pred_p * sys_C + r_noise))
    
    curr_est = pred_x + k_gain * (obs_y[i] - sys_C * pred_x)
    curr_p = (1 - k_gain * sys_C) * pred_p
    
    kalman_est[i] = curr_est
    cov_hist[i] = curr_p
    gain_hist[i] = k_gain

plt.figure(figsize=(11, 9))

plt.subplot(3, 1, 1)
plt.plot(actual_x, label='Actual State', color='dodgerblue', linewidth=2)
plt.scatter(range(time_steps), obs_y, label='Measured Data', color='tomato', alpha=0.45, s=25)
plt.plot(kalman_est, label='Estimated State', color='forestgreen', linestyle='--', marker='.', markersize=7)
plt.title('Kalman Filter Process')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.subplot(3, 1, 2)
plt.plot(gain_hist, label='K Gain', color='rebeccapurple', linewidth=2)
plt.title('Gain over Time')
plt.ylabel('K Value')
plt.grid(True, linestyle=':', alpha=0.7)

plt.subplot(3, 1, 3)
plt.plot(cov_hist, label='Covariance (P)', color='darkorange', linewidth=2)
plt.title('Error Covariance')
plt.xlabel('Time Step')
plt.ylabel('P Value')
plt.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.savefig('ex4.png', dpi=300, bbox_inches='tight')
plt.show()