N = int(input('Введите количество контактов в телефонной книге:\n'))
dictionary = {}
for i in range(N):
    key = int(input(f'Введите номер телефона {i + 1}-го контакта:\n'))
    value = input('Введите пользователя:\n')
    dictionary[key] = value
result = list(dictionary.values())
print(result)
