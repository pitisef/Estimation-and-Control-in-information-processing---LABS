#For each value of r calculate the population size and plot the data r = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]Consider the above vector as values of r measured yearly across 17 years. 
# Answer the question What will bee the population growth in year 17?
import numpy as np
import matplotlib.pyplot as plt

r_list = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]
x = [0.5]  

for r in r_list:
    x_next = r * x[-1] * (1 - x[-1])
    x.append(x_next)

plt.figure(figsize=(10, 5))
plt.plot(x[:9], 'g-o', label="Stable/Fluctuating")
plt.plot(range(8, 18), x[8:], 'r-o', label="Collapse/Instability") 
plt.axhline(0, color='black', lw=1)
plt.title("Population Dynamics (Yearly Variable R)")
plt.xlabel("Year")
plt.ylabel("Population Density (x)")
plt.legend()
plt.grid(True)
plt.show()

print(f"Population at Year 17: {x[17]}")