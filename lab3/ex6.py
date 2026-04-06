import numpy as np
import matplotlib.pyplot as plt

states = ['A', 'B', 'C']
transition_matrix = {
    'A': [0, 0.4, 0.6],
    'B': [0.5, 0.5, 0],
    'C': [0.2, 0.2, 0.6]
}
weights = {'A': 1.5, 'B': 2.0, 'C': 3.3}

current_state = 'A'
s_sequence = [current_state]

for _ in range(14):
    probabilities = transition_matrix[current_state]
    current_state = np.random.choice(states, p=probabilities)
    s_sequence.append(current_state)

r_values = [weights[state] for state in s_sequence]

population = [0.5]
x = 0.5
for r in r_values:
    x = r * x * (1 - x)
    population.append(x)

print("Sequence S:", s_sequence)
print("Growth factors r:", r_values)
print("Population steps:", [round(p, 4) for p in population])

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(s_sequence, 'o-')
plt.title("State Sequence (S)")

plt.subplot(1, 2, 2)
plt.plot(population, 's-r')
plt.title("Population Size")
plt.tight_layout()
plt.show()