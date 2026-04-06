#task 4:
#faulty iot sensors (dependency)
#sensor1 = [1,2]
#sensor2= [2,4]
#Build Matrix A
#check independence of columns
#explain why sistem fails
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2], 
              [2, 4]])

det = np.linalg.det(A)

print("Matrix A:")
print(A)
print("Determinant:", det)

plt.figure(figsize=(5, 5))
plt.plot([0, A[0,0]], [0, A[1,0]], 'r', label='sensor 1 vector', linewidth=3)
plt.plot([0, A[0,1]], [0, A[1,1]], 'b--', label='sensor 2 vector', linewidth=2)
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.legend()
plt.grid(True)
plt.show()


#Why sistem fails?
#The system fails because Sensor 2 doesn't give any new information.
#it is just a multiple of Sensor 1. 
#the matrix is singular and cannot be inverted. 
#You can't solve for two different variablesif the data is redundant.