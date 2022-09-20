N = int(input('Введите количество контактов в телефонной книге:\n'))
phone_book = {}

for i in range(N):
    key = int(input(f'Введите номер телефона {i + 1}-го контакта:\n'))
    value = input('Введите пользователя:\n')
    phone_book[key] = value

result = list(phone_book.values())
print(result)
