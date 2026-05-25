import numpy as np
import matplotlib.pyplot as plt

var_list = [1, 4, 9]
plot_colors = ['crimson', 'teal', 'indigo']

plt.figure(figsize=(9, 5))

for v, c in zip(var_list, plot_colors):
    s = np.sqrt(v)
    data = np.random.normal(0, s, 10000)
    
    lbl = f'Var={v} (Std={s:.1f})'
    plt.hist(data, bins=85, density=True, alpha=0.55, color=c, label=lbl)

plt.title('Gaussian Noise at Varying Variances', fontsize=13)
plt.xlabel('Value', fontsize=11)
plt.ylabel('Density', fontsize=11)
plt.xlim(-11, 11)
plt.legend(fontsize=11)
plt.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('ex5.png', dpi=300)
plt.show()