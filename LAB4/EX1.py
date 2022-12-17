import numpy as np
import matplotlib.pyplot as plt

result = 0
new_result = 0

matrix = np.random.randint(10, size=(6, 6))  # создаем матрицу 6х6 и генерим от 0 до 10
matrix *= 10
matrix = matrix.astype(np.int32, copy=False)  # преобразование элементов
print(matrix)
diagonal = np.diagonal(matrix)
print(f"\nГлавная диагональ:\n{diagonal}\n")
antidiagonal = np.fliplr(matrix).diagonal()
print(f"Побочная диагональ:\n{antidiagonal}\n")
sum_of_diagonales = diagonal + antidiagonal
for i in sum_of_diagonales:
    result += i
print(f"Сумма элементов диагоналей:\n{result}\n")

new_matrix = np.zeros((5, 5), dtype=int)
new_matrix[1::2, ::2] = 8
new_matrix[::2, 1::2] = 8
new_matrix[new_matrix == 0] = 3
print(new_matrix)
new_diagonal = np.diagonal(new_matrix)
print(f"\nГлавная диагональ:\n{new_diagonal}\n")
new_antidiagonal = np.fliplr(new_matrix).diagonal()
print(f"Побочная диагональ:\n{new_antidiagonal}\n")
sum_of_diagonales = new_diagonal + new_antidiagonal
for i in sum_of_diagonales:
    new_result += i
print(f"Сумма элементов диагоналей:\n{new_result}\n")

array1 = [1, 2]
array2 = [result, new_result]

fig = plt.figure()
plt.bar(array1, array2)
plt.title("Diagram")
plt.grid(True)
plt.show()
