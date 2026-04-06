import numpy as np
import matplotlib.pyplot as plt

R_values = np.linspace(2.5, 4.0, 2000)
iterations = 1000
last_points = 100
x = 0.5 * np.ones_like(R_values)

plt.figure(figsize=(10, 6))

for i in range(iterations):
    x = R_values * x * (1 - x)
    if i >= (iterations - last_points):
        plt.plot(R_values, x, ',k', alpha=0.1)

plt.axvline(x=3.57, color='red', linestyle='--')
plt.title("Bifurcation Diagram: Transition to Chaos")
plt.xlabel("Growth Factor (R)")
plt.ylabel("Population Equilibrium")
plt.grid(False)
plt.show()

r_chaos = 3.9
steps = 100
pop = np.zeros(steps)
pop[0] = 0.5
for t in range(steps - 1):
    pop[t+1] = r_chaos * pop[t] * (1 - pop[t])

plt.figure(figsize=(10, 4))
plt.plot(pop, 'b-', linewidth=1)
plt.title(f"Chaotic Time Series (R = {r_chaos})")
plt.xlabel("Time Step")
plt.ylabel("Population")
plt.show()