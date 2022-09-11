from random import randint

size = int(input('Введите размерность матрицы:\n'))

matrix = [[randint(0, 0) for i in range(size)] for j in range(size)]

for i in range(size):
    for j in range(size):
        if (i >= j):
            matrix[i][j] = i - j + 1

for i in range(size):
    print(matrix[i], end='\n')
