number = int(input('Введите натуральное число:\n'))
k = int(input('Введите число разрядов:\n'))

result = 0

for i in range(k):
    result += number % 10
    number = number // 10

print(f'Сумма младших правых {k} разрядов равна: {result}\n')
