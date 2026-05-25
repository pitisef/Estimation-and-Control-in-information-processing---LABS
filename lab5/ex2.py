import numpy as np
import matplotlib.pyplot as plt

data_points = np.random.uniform(0, 1, 1000)

plt.hist(data_points, bins=25, color='coral', edgecolor='black')
plt.title('Uniform Distribution Histogram')
plt.xlabel('X Values')
plt.ylabel('Count')
plt.savefig('output2.png', dpi=300, bbox_inches='tight')
plt.show()