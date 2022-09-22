from random import random, randint

N = int(input('Введите размерность массива:\n'))
lst = [random() for i in range(N)]
lst[-1] = 0
print(f'Исходный массив:\n{lst}')

average = sum(lst) / len(lst)
print(f'Среднее значение:\n{average}')

for position, value in enumerate(lst):
    if value == 0:
        lst[position] = average

print(f'Измененный массив:\n{lst}')
