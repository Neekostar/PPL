from random import randint

A = [randint(-5, 41) for i in range(75)]
Y = []
for i in A:
    if (i < 20):
        Y.append(i)
print(f'Исходный массив:\n{A}\n')
print(f'Результат:\n{Y}')
