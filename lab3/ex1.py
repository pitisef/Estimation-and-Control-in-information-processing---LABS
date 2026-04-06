#make a simulation by using the logistic regresion expressiion( = population  growth)
#use a growth factor R equal to 0.9, make a raport (word doc) wich describes the fate of
#population for R = 0.9

import numpy as np
import matplotlib.pyplot as plt

R = 0.9
x0 = 0.5
steps = 50

pop = np.zeros(steps)
pop[0] = x0

for t in range(steps - 1):
    pop[t+1] = R * pop[t] * (1 - pop[t])

plt.figure(figsize=(8, 5))
plt.plot(pop, 'r-o', markersize=4)
plt.title(f"Population Trend (R = {R})")
plt.xlabel("Time Step")
plt.ylabel("Population Density")
plt.grid(True)
plt.show()

print(f"Final Value: {pop[-1]}")