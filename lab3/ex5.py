#make a series of experiments in which the population number  starts from a) 0.1 b) 0.5 c)1.0 d) 2
#make a repeat in which you note the observations for r=4
import numpy as np
import matplotlib.pyplot as plt

r = 4
steps = 50
starts = [0.1, 0.5, 1.0, 2.0]

plt.figure(figsize=(10, 5))

for start in starts:
    values = [start]
    x = start
    for _ in range(steps):
        x = r * x * (1 - x)
        if abs(x) > 100: 
            x = np.nan
        values.append(x)
    
    plt.plot(values, label=f'Start: {start}')

plt.ylim(-1, 2) 
plt.axhline(0, color='black', lw=1)
plt.legend()
plt.show()