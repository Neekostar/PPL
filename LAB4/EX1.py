import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

matrix = np.random.random((5, 5))
matrix *= 10
print(matrix)
matrix = matrix.astype(np.int32, copy=False)
print(matrix)
determinant = linalg.det(matrix)
print(determinant)
inverse_matrix = linalg.inv(matrix)
inverse_matrix = inverse_matrix.astype(np.int32, copy=False)
print(inverse_matrix)
inverse_matrix_determinant = linalg.det(inverse_matrix)
print(inverse_matrix_determinant)
array1 = [1, 2]
array2 = [determinant, inverse_matrix_determinant]

fig = plt.figure()
plt.bar(array1, array2)
plt.title("Diagram")
plt.grid(True)
plt.show()
