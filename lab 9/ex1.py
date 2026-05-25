import numpy as np
import matplotlib.pyplot as plt

time_steps = 30
sys_A = 1
sys_B = 1
sys_C = 1
ctrl_input = 1
init_x = 0

proc_noise = 0.5
meas_noise = 1.0

actual_state = np.zeros(time_steps)
obs_output = np.zeros(time_steps)

state_x = init_x

for step in range(time_steps):
    actual_state[step] = state_x
    
    v_noise = np.random.normal(0, meas_noise)
    obs_output[step] = sys_C * state_x + v_noise
    
    w_noise = np.random.normal(0, proc_noise)
    state_x = sys_A * state_x + sys_B * ctrl_input + w_noise

plt.figure(figsize=(11, 6))
plt.plot(range(time_steps), actual_state, label='Actual (x)', color='navy', linewidth=2.5)
plt.scatter(range(time_steps), obs_output, label='Observed (y)', color='crimson', alpha=0.75, marker='x')

plt.title('Dynamic System Simulation')
plt.xlabel('Time (t)')
plt.ylabel('System Value')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.savefig('ex1.png', dpi=300, bbox_inches='tight')
plt.show()