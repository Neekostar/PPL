N = int(input('Введите размерность массива:\n'))
lst = []

for i in range(N):
    element = int(input(f'Введите {i + 1} элемент массива:\n'))
    lst.append(element)

print(f'Исходный массив:\n{lst}')

max_element = max(lst)
lst = sorted(lst, reverse=True)

print(f'Отсортированный массив:\n{lst}\nМаксимальный элемент:\n{max_element}')
