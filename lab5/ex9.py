import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
num_pts = 10000

data_x = np.random.normal(0, 1, num_pts)
data_y = 0.7 * data_x + np.random.normal(0, 0.714, num_pts)

cond_a = data_x > 0
cond_b = data_y > 0

prob_a = np.mean(cond_a)
prob_b = np.mean(cond_b)
prob_a_b = np.mean(cond_a & cond_b)
prob_a_given_b = prob_a_b / prob_b

print(f"Prob(A): {prob_a:.4f}")
print(f"Prob(B): {prob_b:.4f}")
print(f"Prob(A&B): {prob_a_b:.4f}")
print(f"Prob(A|B): {prob_a_given_b:.4f}")

fig, (fig1, fig2) = plt.subplots(1, 2, figsize=(13, 6))

fig1.scatter(data_x[~(cond_a | cond_b)], data_y[~(cond_a | cond_b)], alpha=0.15, color='silver', label='None')
fig1.scatter(data_x[cond_a & ~cond_b], data_y[cond_a & ~cond_b], alpha=0.25, color='dodgerblue', label='Only A')
fig1.scatter(data_x[~cond_a & cond_b], data_y[~cond_a & cond_b], alpha=0.25, color='limegreen', label='Only B')
fig1.scatter(data_x[cond_a & cond_b], data_y[cond_a & cond_b], alpha=0.35, color='tomato', label='Both A & B')

fig1.axvline(0, color='gray', linestyle='-', linewidth=1.5)
fig1.axhline(0, color='gray', linestyle='-', linewidth=1.5)

fig1.set_title('Event Simulation Scatter')
fig1.set_xlabel('X Values')
fig1.set_ylabel('Y Values')
fig1.legend()

bar_labels = ['P(A)', 'P(B)', 'P(A&B)', 'P(A|B)']
bar_vals = [prob_a, prob_b, prob_a_b, prob_a_given_b]
bar_colors = ['dodgerblue', 'limegreen', 'tomato', 'mediumorchid']

fig2.bar(bar_labels, bar_vals, color=bar_colors, edgecolor='black', alpha=0.8)

for idx, val in enumerate(bar_vals):
    fig2.text(idx, val + 0.02, f"{val:.3f}", ha='center', fontweight='bold')

fig2.set_ylim(0, 1.15)
fig2.set_title('Probability Estimates')
fig2.set_ylabel('Calculated Probability')

plt.tight_layout()
plt.savefig('ex9.png', dpi=300, bbox_inches='tight')
plt.show()