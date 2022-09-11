str = input('Введите текст, состоящий только из цифр и букв:\n')

digits = []

str.split()
for i in str:
    if i.isdigit():
        digits.append(int(i))

sum = 0
for i in digits:
    sum += i

str_length = len(str)
print(f'Длина текста:\n{str_length}')
print(f'Сумма цифр:\n{sum}')
if (sum == str_length):
    print('Длина текста совпадает с суммой цифр')
else:
    print('Длина текста не совпадает с суммой цифр')
