#using results from lab2
#compute predicted values ax
#compute residual r= y-ax
#compute squared error

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
y = np.array([40, 42, 45])

A = np.array([[1, 1], [2, 1], [3, 1]])
Y = y.reshape(-1, 1)

theta = np.linalg.lstsq(A, Y, rcond=None)[0]
a, b = theta[0][0], theta[1][0]

y_hat = A @ theta
r = Y - y_hat
sse = np.sum(r**2)

print(f"predict y:\n{y_hat.flatten()}")
print(f"residuals:\n{r.flatten()}")
print(f"sum of squared errors: {sse:.4f}")

plt.scatter(x, y, color='red', label='actual')
plt.plot(x, y_hat, color='blue', label='model')
plt.vlines(x, y_hat.flatten(), y, colors='gray', linestyles='dashed', label='residuals')
plt.legend()
plt.grid(True)
plt.show()