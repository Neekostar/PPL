str = input('Введите строку:\n')
str = str.replace(':', '%')
count = str.count('%')
print(f'Строка после обработки:\n{str}\nКоличество замен:\n{count}')
