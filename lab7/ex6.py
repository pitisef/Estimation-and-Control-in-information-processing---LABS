#task 6 iot noise analysis
#errors: [-1,2,-2]
#compute squared error
#compare with abosolute error
#explain impact on decisions

import numpy as np
import matplotlib.pyplot as plt

errors = np.array([-1, 2, -2])

sq_errors = errors**2
abs_errors = np.abs(errors)

print("squared errors:", sq_errors)
print("sum-squared error:", np.sum(sq_errors))
print("absolute errors:", abs_errors)
print("sum-absolute error:", np.sum(abs_errors))

labels = ['error 1', 'error 2', 'error 3']
x = np.arange(len(labels))

plt.bar(x - 0.2, abs_errors, 0.4, label='Absolute', color='blue')
plt.bar(x + 0.2, sq_errors, 0.4, label='Squared', color='orange')

plt.xticks(x, labels)
plt.ylabel('magnitude')
plt.title('absolute vs squared error analysis')
plt.legend()
plt.grid(axis='y', linestyle='--')
plt.show()