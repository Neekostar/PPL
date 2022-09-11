from random import randint

size = 26
s = [randint(0, 100) for i in range(size)]
result = [[], []]

for position, value in enumerate(s):

    if (position % 2 == 0):
        result[0].append(value)
    else:
        result[1].append(value)

print(f'Исходный массив:\n{s}\n')
print('Результат:')
for i in range(2):
    for j in range(13):
        print(result[i][j], end='\t')
    print()

